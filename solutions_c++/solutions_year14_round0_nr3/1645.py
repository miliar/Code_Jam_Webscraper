#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int t,r,c,n,x,y,z,rr;
char ans[60][60];
int dp[51][51][2501];

void solve()
{
    n=r*c-n;
    if(r*c==1&&n==1)
    {
        puts("c");
        return;
    }
    if(n==1)
    {
        //puts("Impossible");
        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++)
                ans[i][j]='*';
        ans[0][0]='c';
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
                printf("%c",ans[i][j]);
            puts("");
        }
        return;
    }
    if(r==1)
    {
        printf("c");
        for(int i=1;i<n;i++)
            printf(".");
        for(int i=n;i<c;i++)
            printf("*");
        puts("");
        return;
    }
    if(c==1)
    {
        printf("c\n");
        for(int i=1;i<n;i++)
            printf(".\n");
        for(int i=n;i<r;i++)
            printf("*\n");
        return;
    }
    memset(dp,0,sizeof(dp));
    for(int i=2;i<=c;i++)
        if(i*2<=n)dp[2][i][2*i]=i;
    for(int i=2;i<r;i++)
    {
        for(int j=c;j>2;j--)
            for(int k=0;k<=n;k++)
                if(dp[i][j][k])
                {
                    dp[i][j-1][k]=dp[i][j][k];
                }
        for(int j=2;j<=c;j++)
            for(int k=0;j+k<=n;k++)
            {
                if(!dp[i][j][k])continue;
                dp[i+1][j][k+j]=j;
            }
    }
    x=-1;
    for(int i=1;i<=r;i++)
        for(int j=1;j<=c;j++)
            if(dp[i][j][n])
            {
                x=i;
                y=j;
                z=n;
            }
    if(x==-1)
    {
        puts("Impossible");
        return;
    }
    memset(ans,'*',sizeof(ans));
    while(x!=2)
    {
        //printf("%d %d %d\n",x,y,z);
        y=dp[x][y][z];
        for(int i=1;i<=y;i++)
            ans[x][i]='.';
        x--;
        z-=y;
    }
    y=dp[x][y][z];
    for(int i=1;i<=y;i++)
        ans[1][i]=ans[2][i]='.';
    ans[1][1]='c';
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=c;j++)
            printf("%c",ans[i][j]);
        puts("");
    }
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c-out.txt","w",stdout);
    //freopen("c-in.txt","r",stdin);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d:\n",cas);
        scanf("%d%d%d",&r,&c,&n);
        solve();
    }
    return 0;
}
