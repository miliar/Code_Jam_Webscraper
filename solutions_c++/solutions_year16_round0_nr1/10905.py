#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int arr[10];

int main()
{
     freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll n,t,i,j,temp,cnt=0,k=1;
    cin>>t;
        for(i=1;i<=t;i++){
                cin>>n;
        if(n==0){
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
                for(j=0;j<=9;j++){
                    arr[j]=0;
                }
         temp=n;
         k=1;
         cnt=0;
         while(1){
            temp=k*n;
            while(temp!=0){
             arr[temp%10]++;
             temp/=10;
            }
            for(j=0;j<=9;j++){
                    if(arr[j]>0){
                        cnt++;
                    }
                }
                if(cnt==10){
                    break;
                }
         //   cout<<cnt<<endl;
            cnt=0;
            k++;
         }

         cout<<"Case #"<<i<<": "<<n*k<<endl;
    }

}
