#include <bits/stdc++.h>
#define LL long long int
#define mod 1000000007
using namespace std;
long long int t,p=0,temp;
int main(){
    std::ios_base::sync_with_stdio(false);
    ofstream outputFile("out.txt");
    cin>>t;
    while(t--){


        int n;
        cin>>n;

        vector < pair < int ,string> > v(n+1);

        //cout << v[0].first << " " << v[0].second << endl;

        int a=65;
        //cout<<"out";
        for(int i=0;i<n;i++){
          //  cout<<"in"<<i<<n;
            cin >> v[i].first;
            v[i].second=(char)a;
            a++;
            //cout<<i<<n;
        }
//        cout<<i<<n;
        outputFile<<"Case #"<<(p+1)<<": ";
        cout<<"Case #"<<(p+1)<<": ";


        sort(v.begin(),v.end(),greater < pair <int,string> >());

        while(v[0].first>1){
            if((v[0].first-v[1].first)>=2){
                v[0].first=v[0].first-2;
                outputFile<<v[0].second<<v[0].second<<" ";
                cout<<v[0].second<<v[0].second<<" ";


            }
            if((v[0].first-v[1].first)<=1){
                v[0].first=v[0].first-1;
                v[1].first=v[1].first-1;;
                outputFile<<v[0].second<<v[1].second<<" ";
                cout<<v[0].second<<v[1].second<<" ";


            }

           sort(v.begin(),v.end(),greater < pair <int,string> >());
        }
        int c=0;
        for(int i=0;i<n;i++){
            if(v[i].first>0)
              c++;

        }
        int j=0;
        if((c%2)!=0){
            outputFile<<v[0].second<<" ";
            cout<<v[0].second<<" ";
            j=1;
        }
        else
            j=0;

        for( ;j<c;j++){
            outputFile<<v[j].second<<v[j+1].second<<" ";
            cout<<v[j].second<<v[j+1].second<<" ";
            j++;
        }


        //cout << v[i].first << " " << v[i].second << endl;


        //outputFile<<"Case #"<<(p+1)<<": "<<t1<<endl;
        //cout<<"Case #"<<(p+1)<<": "<<t1<<endl;
        //cout<<"Case #"<<(p+1)<<": "<<s<<endl;
        //outputFile<<"Case #"<<(p+1)<<": "<<s<<endl;

        p++;
        outputFile<<endl;
        cout<<endl;
    }
outputFile.close();

return 0;
}
