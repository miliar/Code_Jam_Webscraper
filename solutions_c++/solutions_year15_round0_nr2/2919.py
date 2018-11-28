#include <bits/stdc++.h>

using namespace std;

const int Nmax = 1000;
const int INF = 1e9;

int T, P, D;
int ap[Nmax + 3];
int dp[Nmax + 3][Nmax + 3];

int costReducere(int i, int m)
{
    if (dp[i][m] != -1)
        return dp[i][m];

    if (i <= m)
        return 0;

    int a = 1 + costReducere(i / 2, m) + costReducere(i - i / 2, m);
    int b = 1 + costReducere(i - m, m);

    return dp[i][m] = min(a, b);
}

int main()
{
    ifstream in("large.in");
    ofstream out("data.out");

    for (int i = 0; i <= Nmax; ++i)
        for (int j = 0; j <= Nmax; ++j)
            dp[i][j] = -1;

    in >> T;

    for (int t = 1; t <= T; ++t)
    {
        for (int i = 0; i <= Nmax; ++i)
            ap[i] = 0;

        in >> D;

        for (int i = 1; i <= D; ++i)
        {
            in >> P;
            ap[P]++;
        }

        int best = INF;

        for (int m = 1; m <= Nmax; ++m) /// setez maximul la m
        {
            int sol = m;

            for (int i = m + 1; i <= Nmax; ++i)
            {
                if (ap[i])
                {
                    sol += ap[i] * costReducere(i, m);
                }
            }

            best = min(best, sol);
        }

        out << "Case #" << t << ": " << best << "\n";
    }

    return 0;
}
