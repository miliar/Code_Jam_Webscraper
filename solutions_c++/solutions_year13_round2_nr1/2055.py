#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#define MAXN 105
#define INF 1000000000
using namespace std;
int S,N,a[MAXN],dp[MAXN];
void BT(int s,int x,int sum)
{
    //cout<<x<<" "<<s<<" "<<dp[N]<<" "<<sum<<"\n";
    if(x==N+1) return;
    if(s>a[x])
    {
        dp[x]=min(dp[x],sum);
        BT(s+a[x],x+1,sum);
    }
    else
    {
        //if(s+s-1<=a[x])
        //{
        dp[x]=min(dp[x],sum+1);
        BT(s,x+1,sum+1);
        if(s==1)
            return;

            int tmp=s,tmpS=s,cnt=1;
            while(tmpS+tmp-1<=a[N])
            {
                //if(cnt>N-x+3) return;
                tmpS+=tmp-1;
                if(tmpS>a[x])
                {
                    dp[x]=min(dp[x],sum+cnt);
                    BT(tmpS,x,sum+cnt);
                    return;
                }
                //dp[x]=min(dp[x],sum+cnt+1);
                //BT(tmpS,x+1,sum+cnt+1);
                tmp=tmpS;
                cnt++;
            }
            dp[x]=min(dp[x],sum+cnt);
            BT(tmpS+tmp-1,x,sum+cnt);
        //}
        /*if(s+s-1>a[x])
        {
            dp[x]=min(dp[x],sum+1);
            BT(s+s-1,x,sum+1);
        }*/

    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,T;
    scanf("%d",&t);
    T=t;
    while(t--)
    {
        scanf("%d%d",&S,&N);
        for(int i=0;i<MAXN;++i)
            dp[i]=INF;
        for(int i=1;i<=N;++i)
            scanf("%d",&a[i]);
        sort(a+1,a+N+1);
        dp[0]=0;
        BT(S,1,0);
        printf("Case #%d: %d\n",T-t,dp[N]);
    }
    return 0;
}
