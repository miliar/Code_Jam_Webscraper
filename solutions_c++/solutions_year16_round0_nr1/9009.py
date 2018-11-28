#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputl.o","w",stdout);
    int i,T,j;
    long long int N,k,m;
    cin>>T;
    for(i=0;i<T;i++){
        int arr[10]={0},flag=0;
        cin>>N;
        if(N==0){cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;}
        else{
        for(j=1;j<100;j++){
            m=k=j*N;
            while(k>0){
                if(arr[k%10]==0){arr[k%10]++;flag++;}
                k/=10;
            }
        if(flag==10){cout<<"Case #"<<i+1<<": "<<m<<endl;break;}
        }
        }

    }
}
