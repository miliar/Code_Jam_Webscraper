#include <iostream>
#include <cstdio>
#define f cin
#define g cout

using namespace std;

int T;
int N, R, C;
int cnt[2];

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

bool ok (int r, int c)
{
    return (1<=r && r<=R && 1<=c && c<=C);
}

int solve (int N, int where)
{
    int cnt[5] = {0, 0, 0, 0, 0};

    for (int i=1; i<=R; i++)
        for (int j=1; j<=C; j++)
            if ((i+j)%2==where)
            {
                int v = 0;
                for (int d=0; d<4; d++)
                    v += ok(i + dx[d], j+dy[d]);
                cnt[v]++;
            }

    int ans = 0;
    for (int i=0; i<=4; i++)
    {
        ans += i*min(N, cnt[i]);

        N -= min(N, cnt[i]);
    }

    return ans;
}

int main ()
{
    #ifndef ONLINE_JUDGE
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif

    f >> T;
    for (int t=1; t<=T; t++)
    {
        f >> R >> C >> N;

        cnt[0]=cnt[1]=0;
        for (int i=1; i<=R; i++)
            for (int j=1; j<=C; j++)
                cnt[(i+j)%2]++;

        if (N<=cnt[0] || N<=cnt[1])
        {
            g << "Case #" << t << ": " << 0 << '\n';
            continue;
        }

        int ans = min(solve(N-cnt[0], 1), solve(N-cnt[1], 0));
        g << "Case #" << t << ": " << ans << '\n';
    }

    return 0;
}


