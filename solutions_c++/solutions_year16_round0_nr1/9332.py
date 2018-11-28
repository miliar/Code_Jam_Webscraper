#include<bits/stdc++.h>
using namespace std;

#define l long long

ifstream fin("input.txt");
ofstream fout("output.txt");
int main(){
    int t;cin>>t;
    for(int j=1;j<=t;j++){

        l n;cin>>n;
        l temp=n;

        map<l,bool>mark;
        set<int>set1;

        bool ans=false;
        while(true){
            if(mark[n])break;

            l num=n;
            while(num){
                set1.insert(num%10);num/=10;
            }

            if(set1.size()==10){
                ans=true;
                break;
            }

            mark[n]=true;n+=temp;
        }
        cout<<"Case #"<<j<<": ";
        if(ans)cout<<n<<endl;
        else cout<<"INSOMNIA"<<endl;
    }
}
