#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

char maps[105][105];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int R, C;
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                scanf(" %c", &maps[i][j]);
            }
        }
        int ans = 0;
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                if (maps[i][j] == '.') continue;
                int flag = 0;
                for (int k = 0; k < i; k++)
                    if (maps[k][j] != '.') flag |= (1 << 1);
                for (int k = i + 1; k < R; k++)
                    if (maps[k][j] != '.') flag |= (1 << 3);
                for (int k = 0; k < j; k++)
                    if (maps[i][k] != '.') flag |= (1 << 0);
                for (int k = j + 1; k < C; k++)
                    if (maps[i][k] != '.') flag |= (1 << 2);
                if (flag == 0) {ans = -1; break;}
//                cout<<flag<<" "<<maps[i][j]<<endl;
                switch(maps[i][j])
                {
                case '>':
                    if (((flag >> 2) & 1) == 0) ans++;
                    break;
                case '<':
                    if (((flag >> 0) & 1) == 0) ans++;
                    break;
                case '^':
                    if (((flag >> 1) & 1) == 0) ans++;
                    break;
                case 'v':
                    if (((flag >> 3) & 1) == 0) ans++;
                    break;
                default:
                    break;
                }
            }
            if (ans == -1) break;
        }
        if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", cas);
        else printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
