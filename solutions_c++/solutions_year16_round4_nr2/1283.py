#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#define xx first
#define yy second
#define mp(a,b) make_pair(a,b)
using namespace std;
typedef pair<int,int>p1;
typedef  double db;
db dp[9][9];
db a[206];
int cnt[200005];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,k,N=0;
    cin>>t;
    for(int i=1;i<=200000;i++) cnt[i]=cnt[i&(i-1)]+1;
    while(t--){
        cin>>n>>k;
        for(int i=0;i<n;i++) scanf("%lf",&a[i]);
        int p=1<<n;
        db ans=0;
        for(int i=0;i<p;i++){
            if(cnt[i]==k){
                memset(dp,0,sizeof(dp));
                int cnt=0;
                dp[0][0]=1;
                for(int j=0;j<n;j++){
                    if(i&(1<<j)){
                        cnt++;
                        for(int f=min(cnt-1,k/2);f>=0;f--){
                            if(cnt-1-f<=k/2){
                                int q=cnt-1-f;
                                dp[f+1][q]+=dp[f][q]*a[j];
                                dp[f][q+1]+=dp[f][q]*(1-a[j]);
                            }
                        }
                    }
                }
                ans=max(ans,dp[k/2][k/2]);
            }
        }
        printf("Case #%d: %.6lf\n",++N,ans);
    }
}