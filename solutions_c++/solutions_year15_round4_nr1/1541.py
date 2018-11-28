# include <bits/stdc++.h>
using namespace std;
ifstream fi("a.in");
ofstream fo("a.out");
char s[105][105];
bool v[105][105];
bool b[105][105];
int n,m;
const char tl[] = {'^','v','<','>'};
int nx(int x,char c)
{
    if (c == '^') return x-1;
    if (c == 'v') return x+1;
    return x;
}
int ny(int y,char c)
{
    if (c == '<') return y-1;
    if (c == '>') return y+1;
    return y;
}
bool ok = 1;
int ans = 0;
bool go(int x,int y,char c)
{
    if (x < 1 || x > n || y < 1 || y > m) return 0;
    if (s[x][y] == '.') return go(nx(x,c),ny(y,c),c);
    if (v[x][y]) return 1;
    v[x][y] = 1;
    bool p = go(nx(x,s[x][y]),ny(y,s[x][y]),s[x][y]);
    if (p) return 1;
    if (!ok) return 0;
    v[x][y] = 0;
    for (int k = 0;k < 4;++k)
        if (tl[k] != s[x][y])
        {
             v[x][y] = 1;
             bool p = go(nx(x,tl[k]),ny(y,tl[k]),tl[k]);
             if (p) return ++ans,1;
             if (!ok) return 0;
             v[x][y] = 0;
        }
    ok = 0;
}
int main(void)
{
    int t;
    fi>>t;
    for (int cas = 1;cas <= t;++cas)
    {
        ok = 1;ans = 0;
        fi>>n>>m;
        for (int i = 0;i < 105;++i) for (int j = 0;j < 105;++j) v[i][j] = 0,s[i][j] = 0;
        for (int i = 1;i <= n;++i) fi>>(s[i]+1);
        for (int i = 1;i <= n;++i)
            for (int j = 1;j <= m;++j)
               if (s[i][j] != '.' && !v[i][j]) go(i,j,0);
        fo << "Case #" << cas << ": ";
        if (ok) fo << ans << '\n';
        else fo << "IMPOSSIBLE\n";
    }
    return 0;
}
