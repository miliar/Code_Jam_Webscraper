#include <iostream>
#include <cstdio>
#define f cin
#define g cout
#define NM 110

using namespace std;

int R, C;
char A[NM][NM];

bool ok (int x, int y)
{
    return (1<=x && x<=R && 1<=y && y<=C);
}

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};
// 0 up
// 1 right
// 2 down
// 3 left

int dir[3000];

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int T;
    f >> T;

    dir['^'] = 0;
    dir['v'] = 2;
    dir['<'] = 3;
    dir['>'] = 1;

    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";
        f >> R >> C;
        for (int i=1; i<=R; i++)
            f >> (A[i]+1);

        bool possible = true;
        int ans = 0;

        for (int i=1; i<=R && possible; i++)
            for (int j=1; j<=C && possible; j++)
                if (A[i][j] != '.')
                {
                    int d = dir[A[i][j]];
                    bool stopped = false;
                    int x = i+dx[d];
                    int y = j+dy[d];

                    while (ok(x, y))
                    {
                        if (A[x][y] != '.')
                            stopped = true;
                        x+=dx[d];
                        y+=dy[d];
                    }

                    if (stopped == false)
                    {
                        ans++;

                        stopped = false;
                        for (d=0; d<4; d++)
                        {
                            x = i+dx[d];
                            y = j+dy[d];

                            while (ok(x, y))
                            {
                                if (A[x][y] != '.')
                                    stopped = true;
                                x+=dx[d];
                                y+=dy[d];
                            }
                        }
                        if (stopped == false)
                            possible = false;
                    }
                }

        if (possible)
            g << ans << '\n';
        else
            g << "IMPOSSIBLE\n";
    }

    return 0;
}




