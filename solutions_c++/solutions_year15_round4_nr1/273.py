#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 110;
const int dx[4] = {0,-1,0,1};
const int dy[4] = {1,0,-1,0};
bool vis[N][N];
char ch[N][N];
int r,c;
int dir[300];
void init()
{
    dir['^'] = 1;
    dir['>'] = 0;
    dir['<'] = 2;
    dir['v'] = 3;
}
bool ok1(int x,int y)
{
    if (x < 1 || x > r || y < 1 || y > c) return 0;
    return 1;
}
bool ok2(int x,int y)
{
    if (ch[x][y] == '>' || ch[x][y] == '<' || ch[x][y] == '^' || ch[x][y] == 'v') return 1;
    return 0;
}
int dfs(int x,int y,int k)//
{
    int xx = x + dx[k];
    int yy = y + dy[k];

    if (ok1(xx,yy))
    {
        if(ok2(xx,yy)) return 0;
    }

    while (ch[xx][yy] == '.')
    {
        if (ok1(xx,yy))
        {
            if(ok2(xx,yy)) return 0;
        }
        else
            break;
        xx = xx + dx[k];
        yy = yy + dy[k];
    }

    if (ok1(xx,yy))
    {
        if(ok2(xx,yy)) return 0;
    }

    for (int i = 0; i < 4; i++)
        if (i != k)
        {
            xx = x + dx[i];
            yy = y + dy[i];
            if (ok1(xx,yy))
            {
                //printf("%d %d %c\n",xx,yy,ch[xx][yy]);
                if(ok2(xx,yy)) return 1;
            }
            else
                continue;

            while (ch[xx][yy] == '.')
            {
                if (ok1(xx,yy))
                {
                    if(ok2(xx,yy)) return 1;
                }
                else
                    break;
                xx = xx + dx[i];
                yy = yy + dy[i];

            }
            if (ok1(xx,yy))
            {
                if(ok2(xx,yy)) return 1;
            }
        }
    return -1;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    init();
    int t;
    scanf("%d",&t);
    while (t--)
    {
        memset(vis,0,sizeof vis);
        static int ca = 0;
        printf("Case #%d: ",++ca);
        scanf("%d%d",&r,&c);
        for (int i = 1; i <= r; i++) scanf("%s",ch[i]+1);
        int ans = 0;
        int flag = 1;
        for (int i = 1; i <= r && flag; i++)
        {
            for (int j = 1; j <= c && flag; j++)
                if (ch[i][j] != '.' && vis[i][j] == 0)
                {
                    //printf("%d %d\n",i,j);
                    int tmp = dfs(i,j,dir[ch[i][j]]);
                    // printf("tmp %d\n",tmp);
//                    if (tmp == 1 && ca == 1)
//                        printf("%d %d\n",i,j);
                    if (tmp == -1)
                    {
                        flag = 0;
                    }
                    else
                        ans += tmp;
                }
        }
        if (flag)
            printf("%d\n",ans);
        else
            puts("IMPOSSIBLE");
    }
}
