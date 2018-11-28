#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;
vector<long long>divi[3000];
const long long MOD=1000000007;
long long dp[2][3000],n,K,sz[3000];
int main(){
    memset(sz,0,sizeof(sz));
    cin>>K>>n;
    for(long long j=1;j<=K;j++)
        for(long long i=1;i<=j;i++)
            if(j%i==0) {
                divi[j].push_back(i);
                sz[j]++;
            }
    bool cur=0;
    memset(dp,0,sizeof(dp));
    dp[cur][1]=1;
    for(long long cnt=1;cnt<=n;cnt++){
        cur=!cur;
        for(long long j=1;j<=K;j++){
            dp[cur][j]=0;
            for(long long i=0;i<sz[j];i++){
                dp[cur][j]+=dp[!cur][divi[j][i]];
                dp[cur][j]%=MOD;
            }
         //   cout<<cnt<<' '<<j<<' '<<dp[cur][j]<<endl;
        }
    }
    long long ans=0;
    for(long long j=1;j<=K;j++){
        ans+=dp[cur][j];
        ans%=MOD;
        //cout<<j<<' '<<dp[cur][j]<<endl;
    }
    cout<<ans<<endl;
}
