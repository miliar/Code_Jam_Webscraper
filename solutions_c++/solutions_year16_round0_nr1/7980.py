#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("o3.out","w",stdout);
    int t,n,i,j;
    cin>>t;
    for(i=1;i<=t;i++){
       cin>>n;
        if(n==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else {
            int ar[10]={0};
            bool flag=true;
            int temp=n;
            while(flag==true){
                int p=temp;
                while(p>0)
                {
                    ar[p%10]++;
                    p/=10;
                }
                for(j=0;j<10;j++){
                    // cout<<ar[j]<<" ";
                    if(ar[j]==0)
                    break;
                }
                if(j==10)
                    flag=false;
                    if(flag==true)
                        temp+=n;
            }
            cout<<"Case #"<<i<<": "<<temp<<endl;
        }
    }
return 0;
}
