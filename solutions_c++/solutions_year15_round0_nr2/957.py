#include <iostream>
#include <cstdio>
#include <set>
#define f cin
#define g cout
#define NM 2010

using namespace std;

int N;
int V[NM];

int Check (int X)
{
    int cnt = 0;
    int maxi = 0;

    for (int i=1; i<=N; i++)
        if (V[i] > X)
        {
            maxi = X;
            cnt += (V[i] - 1) / X;
        }
        else
            maxi = max(maxi, V[i]);

    return maxi + cnt;
}

int Search ()
{
    int ANS=NM;

    for (int i=1; i<=1010; i++)
        ANS=min(ANS, Check(i));

    return ANS;
}

int main ()
{
    /*
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    /* */

    int T;
    f >> T;

    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";

        f >> N;
        for (int i=1; i<=N; i++)
            f >> V[i];

        g << Search() << '\n';
    }

    return 0;
}
