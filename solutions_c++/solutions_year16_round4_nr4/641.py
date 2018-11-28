#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int dp[16][16];
int vis[16][16];

int arr[4][4];
int arr1[4][4];

int dfs(int n, int m)
{
    if (vis[n][m])
        return dp[n][m];
    if (m==0)
        return 0;
    vis[n][m]=1;
    dp[n][m]=0;
    for (int i=0;i<4;i++)if(m&(1<<i))
    {
        for (int j=0;j<4;j++)if(n&(1<<j))
        {
            if (arr[j][i])
            {
                dp[n][m]=max(dfs(n-(1<<j), m-(1<<i))+1, dp[n][m]);
            }
        }
        dp[n][m]= max(dfs(n, m-(1<<i)), dp[n][m]);
    }
    return dp[n][m];
}

char str[1024];
int main()
{
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n;
        scanf("%d",&n);
        int mask=0;
        for (int i=0;i<n;i++)
        {
            scanf("%s",str);
            for (int j=0;j<n;j++)
            {
                if (str[j]=='0')
                    arr[i][j]=0;
                else
                    arr[i][j]=1, mask|=1<<(i*n+j);
            }
        }
        int ret=-1;
        memcpy(arr1, arr,sizeof(arr));
        for (int m=0;m<(1<<(n*n));m++)if((m&mask)==0)
        {
            int cost=0;
            memcpy(arr, arr1,sizeof(arr));
            for (int i=0;i<n;i++)
                for (int j=0;j<n;j++)if(m&(1<<(i*n+j)))
                {
                    arr[i][j]=1;
                    cost++;
                }
            memset(vis,0,sizeof(vis));
            bool ok = true;
            for (int i=0;i<n;i++)
            {
                int m=0, num=0;
                for (int j=0;j<n;j++)if(arr[i][j])
                    m|=1<<j, num++;
                if (dfs((1<<n)-1-(1<<i), m)==num)
                {
                    ok=false;
                    break;
                }
            }
            if (ok)
            {
                if (ret<0||ret>cost)
                    ret=cost;
            }
        }
        printf("Case #%d: %d\n", ii, ret);
    }
}
