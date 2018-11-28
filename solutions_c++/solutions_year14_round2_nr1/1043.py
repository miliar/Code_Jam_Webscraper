#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#define N 110
#define INF 0x7fffffff
using namespace std;
char s1[N][N],s2[N][N];
int sum[N][N];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    void get(int k);
    int t,T = 1;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<=n-1;i++)
        {
            scanf("%s",s1[i]);
        }
        memset(sum,0,sizeof(sum));
        for(int i=0;i<=n-1;i++)
        {
            get(i);
        }
        bool ch = true;
        for(int i=1;i<=n-1;i++)
        {
            if(strcmp(s2[i],s2[0])!=0)
            {
                ch  = false;
                break;
            }
        }
        printf("Case #%d: ",T++);
        if(!ch)
        {
            printf("Fegla Won\n");
            continue;
        }
        int ans = 0;
        int l = strlen(s2[0]);
        for(int i=0;i<=l-1;i++)
        {
            int Min = INF;
            for(int j=0;j<=n-1;j++)
            {
                int ans = 0;
                for(int u=0;u<=n-1;u++)
                {
                    if(sum[j][i]>sum[u][i])
                    {
                        ans+=(sum[j][i]-sum[u][i]);
                    }else
                    {
                        ans+=(sum[u][i]-sum[j][i]);
                    }
                }
                Min = min(ans,Min);
            }
            ans+=Min;
        }
        printf("%d\n",ans);
    }
    return 0;
}
void get(int k)
{
    int l = strlen(s1[k]);
    s2[k][0] = s1[k][0];
    sum[k][0]++;
    char c = s1[k][0];
    int Top=0;
    for(int i=1;i<=l-1;i++)
    {
        if(s1[k][i]==c)
        {
            sum[k][Top]++;
        }else
        {
            Top++;
            sum[k][Top]++;
            c = s1[k][i];
            s2[k][Top] = c;
        }
    }
    s2[k][Top+1] = '\0';
}
