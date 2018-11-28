
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <set>
#define maxn 20
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

int d[maxn][maxn];
int pre[maxn][maxn];

int pos[(1<<18)+100][maxn];
int dp[(1<<18)+100][maxn];
int bst[(1<<18)+100];
int n,m;
int INF;
vector<int> ans[2];

void DP()
{
    memset(dp,0x3f,sizeof(dp));
    INF = dp[0][0];
    dp[0][0]=0;
    pos[0][0]=0;

    int top = 1<<n;

    for (int i=0;i<top;i++)
        for (int j=0;j<=n;j++)
        if (dp[i][j]!=-1)
        {
            for (int k=1;k<=n;k++)
                if (!(i&(1<<(k-1))))
                {
                    if (dp[i][j]+d[j][k]<dp[(i|(1<<(k-1)))][k])
                    {
                        dp[(i|(1<<(k-1)))][k] = dp[i][j] + d[j][k];
                        pos[(i|(1<<(k-1)))][k] = j;
                    }
                }
        }
}

void findPath(int x,int y,int id)
{
    int now = x;
    do
    {
        now = pre[now][y];
        ans[id].push_back(now);
    } while (now!=y);
}

void output(int st,int k,int id)
{
    int x = pos[st][k];
    if (x!=0)
        output(st^(1<<(k-1)),x,id);
    findPath(x,k,id);
}

int main()
{
    //freopen("/home/py/Desktop/input.txt","r",stdin);
    //freopen("/home/py/Desktop/output.txt","w",stdout);

    scanf("%d%d",&n,&m);
    int x,y,t;

    for (int i=0;i<=n;i++)
        for (int j=0;j<=n;j++)
            d[i][j]=oo,pre[i][j]=-1;

    for (int i=0;i<=n;i++)
        d[i][i]=0,pre[i][i]=i;

    for (int i=1;i<=m;i++)
    {
        scanf("%d%d%d",&x,&y,&t);
        d[x][y]=d[y][x]=t;
        pre[x][y]=y;
        pre[y][x]=x;
    }

    d[0][1]=d[1][0]=0;
    pre[0][1]=1;
    pre[1][0]=0;

    for (int k=0;k<=n;k++)
        for (int i=0;i<=n;i++)
            for (int j=0;j<=n;j++)
            if (d[i][j]>d[i][k]+d[k][j])
            {
                d[i][j]=d[i][k]+d[k][j];
                pre[i][j]=pre[i][k];
            }

    DP();

    int full = (1<<n)-1;

    for (int i=0;i<=full;i++)
    {
        bst[i] = -1;
        for (int j=1;j<=n;j++)
            if (bst[i]==-1||dp[i][j]<dp[i][bst[i]])
            {
                bst[i] = j;
            }
    }

    int best1;
    int best2;
    int tmp1,tmp2;

    int T = oo;

    for (int i=0;i<=full;i++)
    if (dp[i][bst[i]]!=INF)
    {
            tmp1 = i;
            tmp2 = full^i;
            if (bst[tmp2]==-1) continue;

            if (max(dp[tmp1][bst[tmp1]],dp[tmp2][bst[tmp2]])<T)
            {
                best1=tmp1; best2=tmp2;
                T = max(dp[tmp1][bst[tmp1]],dp[tmp2][bst[tmp2]]);
            }
    }

    cout << T <<endl;

    output(best1,bst[best1],0);
    output(best2,bst[best2],1);

    printf("%d",ans[0].size()-1);

    for (int i=0;i<ans[0].size();i++)
        printf(" %d",ans[0][i]);
    printf("\n");


    printf("%d",ans[1].size()-1);

    for (int i=0;i<ans[1].size();i++)
        printf(" %d",ans[1][i]);
    printf("\n");
    return 0;
}
