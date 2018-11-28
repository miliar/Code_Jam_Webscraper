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
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,T = 1;
    scanf("%d",&t);
    while(t--)
    {
        int n,m,k;
        scanf("%d %d %d",&n,&m,&k);
        int ans  = 0;
        for(int i=0;i<=n-1;i++)
        {
            for(int j=0;j<=m-1;j++)
            {
                if((i&j)<k)
                {
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",T++,ans);
    }
    return 0;
}
