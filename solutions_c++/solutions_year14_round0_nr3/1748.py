#include <stdio.h>
#include <cstring>
const int N = 55;
const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
int r, c, m;
int vis[N][N];
int R[N*N], C[N*N];
char ans[N][N];
void mark(int *x, int *y, int num, int c)
{
    for(int i=0; i<num; i++)
    {
        vis[x[i]][y[i]] = c;
    }
}
bool dfs(int cnt)
{
    if(cnt+m==r*c)
    {
        int i, j;
        int si=R[0], sj=C[0];
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                if(i==si && j==sj)  printf("c");
                else if(vis[i][j])  printf(".");
                else    printf("*");
            }
            printf("\n");
        }
        return 1;
    }
    for(int k=0; k<cnt; k++)
    {
        int i = R[k];
        int j = C[k];
        int num = 0;
        int ox[8], oy[8];
        for(int d=0; d<8; d++)
        {
            int x = i+dx[d];
            int y = j+dy[d];
            if(x<0 || x>=r || y<0 || y>=c || vis[x][y])  continue;
            ox[num] = x;
            oy[num] = y;
            R[cnt+num] = x;
            C[cnt+num] = y;
            num++;
        }
        if(0==num || cnt+num+m>r*c)  continue;
        mark(ox, oy, num, 1);
        if(dfs(cnt+num))    return 1;
        mark(ox, oy, num, 0);
    }
    return 0;
}
int main()
{
//    freopen("c.in", "r", stdin);
//    freopen("c.out", "w", stdout);
    int t, kase=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &r, &c, &m);
        printf("Case #%d:\n", ++kase);
        bool no = 1;
        memset(vis, 0, sizeof(vis));
        for(int i=0; i<r && no; i++)
        {
            for(int j=0; j<c && no; j++)
            {
                vis[i][j] = 1;
                R[0] = i;
                C[0] = j;
                if(dfs(1))  no = 0;
                vis[i][j] = 0;
            }
        }
        if(no)  printf("Impossible\n");
    }
    return 0;
}
