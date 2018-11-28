#include<cstdio>
#include<algorithm>

using namespace std;

int T, N, dp[1009][1009], a[1009];

int main ()
{
//freopen ("input", "r", stdin);
//freopen ("output", "w", stdout);

for (int i=1; i<=1000; i++)
    for (int j=1; j<=1000; j++)
    {
        if (i > j)
            dp[i][j] = min (dp[i - i / 2][j] + dp[i / 2][j] + 1, dp[i-j][j] + 1);
        else
            dp[i][j] = 0;
    }

int test = 0;
scanf ("%d", &T);
while (T)
{
    printf ("Case #%d: ", ++test);
    T --;

    int maxi = 0;
    scanf ("%d", &N);
    for (int i=1; i<=N; i++)
    {
        scanf ("%d", &a[i]);
        if (a[i] > maxi)
            maxi = a[i];
    }

    int mini;
    for (int tmax = 1; tmax <= maxi; tmax ++)
    {
        int nr_mutari = 0;
        for (int i=1; i<=N; i++)
            nr_mutari += dp[a[i]][tmax];

        if (tmax == 1)
            mini = nr_mutari + tmax;
        else
        if (nr_mutari + tmax < mini)
            mini = nr_mutari + tmax;
    }

    printf ("%d\n", mini);
}

return 0;
}
