#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int P, Q, N;

long long int table[101][1002];
int hp[101];
int score[101];

long long int f(int n, int r)
{
    if(n == N)
        return 0;
    else if(table[n][r])
        return table[n][r] - 1;
    else
    {
        long long int& v = table[n][r];

        v = f(n + 1, r + (hp[n] + Q - 1) / Q);

        //if(r * P >= hp[n])
        //    v = max(v, f(n + 1, r - (hp[n] + P - 1) / P) + score[n]);

        int nee = (hp[n] + Q - 1) / Q;

        if((nee - 1) * Q + (nee - 1 + r) * P >= hp[n])
        {
            int nee2 = (hp[n] - (nee - 1) * Q + P - 1) / P;
            v = max(v, f(n + 1, r + nee - 1 - nee2) + score[n]);
        }

        return v++;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int ttt = 1; ttt <= T; ttt++)
    {
        printf("Case #%d:", ttt);
        scanf("%d%d%d", &P, &Q, &N);

        for(int i = 0; i < N; i++)
            scanf("%d%d", hp + i, score + i );
        memset(table, 0, sizeof(table));
        printf(" %lld\n", f(0, 1));

    }
    return 0;
}
