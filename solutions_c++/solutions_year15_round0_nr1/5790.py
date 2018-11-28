//Standing Ovation

#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, N, Ans, K;
char S[1005];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d\n", &T);
    for (int Ts = 1; Ts <= T; Ts++)
    {
        scanf("%d %s\n", &N, S);
        Ans = 0;
        K = S[0] - '0';
        for (int i = 1; i <= N; i++)
            if (S[i] != '0')
            {
                int Temp = S[i] - '0';
                if (i > K) Ans += i - K, K += Temp + i - K;
                else K += Temp;
            }
        printf("Case #%d: %d\n", Ts, Ans);
    }
    return 0;
}
