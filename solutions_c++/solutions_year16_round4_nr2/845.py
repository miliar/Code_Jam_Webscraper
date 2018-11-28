#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
using namespace std;
typedef long long ll;
#define mem(name,value) memset(name,value,sizeof(name))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
const int maxn=20,inf=0x3f3f3f3f;

double p[maxn],dp[maxn][maxn];
int n,t;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--){
        printf("Case #%d: ",cas++);
        cin>>n>>t;
        for(int i=0;i<n;i++) scanf("%lf",&p[i]);

        double ans=0;
        int all=(1<<n);
        for(int i=0;i<all;i++){
            vector<double>v;
            for(int j=0;j<n;j++)
                if(i&(1<<j)) v.push_back(p[j]);
            if(v.size()!=t) continue;
            mem(dp,0);dp[0][0]=1;
            for(int j=1;j<=t;j++){
                //cout<<v[j-1]<<endl;
                for(int k=0;k<=j && 2*k<=t;k++){
                    if(k<=j-1) dp[j][k]+=dp[j-1][k]*(1-v[j-1]);
                    if(k) dp[j][k]+=dp[j-1][k-1]*v[j-1];
                }
            }
            ans=max(ans,dp[t][t/2]);
        }

        cout<<ans<<endl;

    }
}











