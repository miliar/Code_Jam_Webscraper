#include <bits/stdc++.h>
#define LL long long int
#define mod 1000000007
using namespace std;
long long int n,t,p=0,temp,t1;
int main(){
    std::ios_base::sync_with_stdio(false);
    ofstream outputFile("out.txt");
    cin>>t;
    while(t--){
        string s="INSOMNIA";
        int k=0;
        int a[10]={0};
        cin>>n;

        for(int i=1;i<1000;i++){
            temp=n*i;
            t1=temp;
            //cout<<temp<<" ";
            //for(int i=1;j<9;j++)
            while(temp!=0){
                a[temp%10]=1;
                temp=temp/10;
            }
            for(int j=0;j<10;j++){

                if(a[j]==1 && j!=9)
                 continue;
                else if(a[j]==1 && j==9)
                 k=1;
                else
                 break;

            }

            if(k==1)
                    break;

        }

        if(k==1){
                    outputFile<<"Case #"<<(p+1)<<": "<<t1<<endl;
                   cout<<"Case #"<<(p+1)<<": "<<t1<<endl;
        }
        else{ cout<<"Case #"<<(p+1)<<": "<<s<<endl;
            outputFile<<"Case #"<<(p+1)<<": "<<s<<endl;
        }
        p++;

    }
outputFile.close();

return 0;
}
