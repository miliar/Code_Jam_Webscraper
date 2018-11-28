#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
int p[100],pre[(1<<20)],step[(1<<20)],dp[(1<<20)];
int a[30],g[30][30],b[30],open[30];
int num[30];
vector <int> way[1<<20];
bool better(int ts,int s,int num)
{
    for (int i=0;i<way[s].size();i++)
    {
        if (way[s][i]<way[ts][i]) return true;
        if (way[s][i]>way[ts][i]) return false;
    }
    return false;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int K,n;
        scanf("%d%d",&K,&n);
        for (int i=0;i<K;i++)
            scanf("%d",&a[i]);
        for (int i=0;i<n;i++)
        {
            scanf("%d%d",&open[i],&b[i]);
            for (int j=0;j<b[i];j++)
                scanf("%d",&g[i][j]);
        }
        memset(dp,0,sizeof(dp));
        dp[0]=1;
        way[0].clear();
        for (int i=0;i<(1<<n);i++)
        {
            if (!dp[i]) continue;
            memset(num,0,sizeof(num));
            for (int j=0;j<K;j++)
                num[a[j]]++;
            for (int j=0;j<n;j++)
            {
                if ((i&(1<<j))==0) continue;
                for (int k=0;k<b[j];k++)
                    num[g[j][k]]++;
                num[open[j]]--;
            }
            for (int j=0;j<n;j++)
            {
                if (i&(1<<j)) continue;
                if (num[open[j]]==0) continue;
                int ts=(i|(1<<j));
                if (dp[ts]==0||better(ts,i,j))
                {
                    pre[ts]=i;
                    step[ts]=j;
                    way[ts].clear();
                    for (int k=0;k<way[i].size();k++)
                        way[ts].push_back(way[i][k]);
                    way[ts].push_back(j);
                    dp[ts]=1;
                }
            }
        }
        printf("Case #%d:",ii);
        int cnt=0;
        if (dp[(1<<n)-1]==0) puts(" IMPOSSIBLE");
        else
        {
            for (int i=0;i<n;i++)
                printf(" %d",way[(1<<n)-1][i]+1);
            puts("");
        }
    }
    return 0;
}

