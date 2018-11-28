#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputll.o","w",stdout);
    int i,T,j;
    long long int N,k,n;
    cin>>T;
    for(i=0;i<T;i++){
        int arr[10]={0},s=0;
        cin>>N;
        if(N==0){cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;}
        else{
        for(j=1;j<100;j++){
            n=k=j*N;
            while(k>0){
                if(arr[k%10]==0){arr[k%10]++;s++;}
                k/=10;
            }
        if(s==10){cout<<"Case #"<<i+1<<": "<<n<<endl;break;}
        }
        }

    }
}
