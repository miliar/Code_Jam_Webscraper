#include<bits/stdc++.h>
using namespace std;
int main(){
int t;
cin>>t;
for(int i=1;i<=t;i++){
    long long n;
    cin>>n;
    if(n==0)
        cout<<"Case #"<<i<<": INSOMNIA\n";
    else{
        bool dp[10]={0};
        for(long long j=1;;j++){
            long long num=j*n;
            while(num){
                int tmp=num%10;
                dp[tmp]=1;
                num/=10;
            }
            int k;
            for(k=0;k<10;k++)if(dp[k]==0)break;
            if(k==10){
                cout<<"Case #"<<i<<": "<<j*n<<"\n";
                break;
            }
        }
    }
}
return 0;
}
