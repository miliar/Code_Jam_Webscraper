#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[111][111];
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

int checker(char a)
{
    return a == '^'?0: a=='<'?1: a=='v'?2: 3;
}

int main(int argv, char** argc)
{
    int T;
    if (argv > 1)
        freopen(argc[1], "r", stdin);
    if (argv > 2)
        freopen(argc[2], "w", stdout);
    scanf("%d",&T);
    for (int t = 1; t <= T; ++t)
    {
        int n, m;
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; ++i)
            scanf("%s", s+i);
        bool flags = true;
        int res = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
            {
                if (s[i][j] != '.')
                {
                    bool p[4], flag = false;
                    for (int k = 0; k < 4; ++k)
                    {
                        int di = i, dj = j;
                        do
                        {
                            di += dx[k], dj += dy[k];
                        } while(0 <= di && di < n && 0 <= dj && dj < m && s[di][dj] == '.');
                        if (di < 0 || di >= n || dj < 0 || dj >= m)
                            p[k] = false;
                        else p[k] = true, flag = true;
                    }
                    flags &= flag;
                    if (!p[checker(s[i][j])]) res++;
                }
            }
        if (flags)
            printf("Case #%d: %d\n", t, res);
        else printf("Case #%d: IMPOSSIBLE\n", t);
    }
}