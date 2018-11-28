#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
char s[150][150];
const int fx[4]= {-1,0,1,0};
const int fy[4]= {0,1,0,-1};
//UP RIGHT DOWN LEFT
bool f[5];
int tt;
int n,m;
bool go(int x,int y,int dir)
{
    int tx,ty;
    tx = x + fx[dir]; ty = y + fy[dir];
    if (tx < 0 || tx >= n) return false;
    if (ty < 0 || ty >= m) return false;
    while(s[tx][ty]=='.')
    {

        tx += fx[dir];
        ty += fy[dir];
        if (tx < 0 || tx >= n) return false;
        if (ty < 0 || ty >= m) return false;
    }
    return true;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tt);
    for (int ii = 1; ii <= tt; ii++)
    {
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; i++)
        {
            scanf("%s",s[i]);
        }

        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
            {
                if (s[i][j] != '.')
                {
                    memset(f,false,sizeof f);
                    bool has = false;
                    for (int k = 0; k < 4; k++)
                    {
                        if (go(i,j,k))
                        {f[k] = true;
                            has = true;
                        }
                    }
                    int ck;
                    if (s[i][j] == '^') ck = 0;
                    if (s[i][j] == '>') ck = 1;
                    if (s[i][j] == 'v') ck = 2;
                    if (s[i][j] == '<') ck = 3;
                    if (!f[ck] && has) ans++;
                    else if (!has)
                    {
                        ans = -999999;
                        i = n+1; j = m+1; break;
                    }
                }
            }
        if (ans < 0) printf("Case #%d: IMPOSSIBLE\n",ii);
        else printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
