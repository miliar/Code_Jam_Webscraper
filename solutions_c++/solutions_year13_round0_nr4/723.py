#include<cstdio>
#include<map>
#include<vector>
#include<cstring>
using namespace std;
int dp[1<<20];
int init[255];

struct node
{
    int kt;
    int nk;
    vector<int> v;
}chest[20];
int nk,n;
int saya(int now)
{
    if (now==(1<<n)-1) return dp[now]=1024;
    int nowk[255];
    //printf("now:%d\n",now);
    if (dp[now]!=-1) return dp[now];
    memset(nowk,0,sizeof(nowk));
    for(int i=0;i<210;i++)
    {
        nowk[i]+=init[i];
    }
    for(int i=0;i<n;i++)
    {
        if ((1<<i)&now)
        {
             nowk[chest[i].kt]--;
            for(int j=0;j<chest[i].v.size();j++)
            {
                nowk[chest[i].v[j]]++;
            }
        }
    }
    //printf("nowk:");
    //for(int i=0;i<n;i++) printf("%d ",nowk[i]);
    //puts("");
    for(int i=0;i<n;i++)
    {
        //printf("i:%d\n",i);
        if ((1<<i)&now) continue;
        if (!nowk[chest[i].kt]) continue;
        if (saya(now|(1<<i))!=-2)
        {
            return dp[now]=i;
        }
    }
    return dp[now]=-2;
}
int main()
{
    freopen("D2.in","r",stdin);
    freopen("D2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int mt=1;mt<=T;mt++)
    {
        memset(init,0,sizeof(init));
        memset(dp,-1,sizeof(dp));
        scanf("%d%d",&nk,&n);
        for(int i=0;i<nk;i++)
        {
            int a;
            scanf("%d",&a);
            init[(a-1)]++;
        }
        for(int i=0;i<n;i++)
        {
            int kt,nk;
            scanf("%d",&kt);
            kt--;
            scanf("%d",&nk);
            chest[i].kt=kt;
            chest[i].v.clear();
            for(int j=0;j<nk;j++)
            {
                int a;
                scanf("%d",&a);
                chest[i].v.push_back(a-1);
            }
        }
        printf("Case #%d:",mt);
        if (saya(0)==-2)
        {
            printf(" IMPOSSIBLE");
        }
        else
        {
            int now=0;
            while(now!=(1<<n)-1)
            {
                printf(" %d",saya(now)+1);
                now|=1<<saya(now);
            }
        }
        puts("");
    }
}
