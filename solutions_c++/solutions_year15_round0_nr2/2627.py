#include <iostream>
#include <cstdio>

using namespace std;

#define INF 2e9

int T, D;
int P[2000];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d", &D);

        for(int Di = 0; Di < D; Di++)
            scanf("%d", &P[Di]);

        int Ans = INF;

        for(int i = 1; i <= 1000; i++)
        {
            int cnt = i;

            for(int Di = 0; Di < D; Di++)
                cnt += (P[Di]-1)/i;

            Ans = min(Ans, cnt);
        }

        printf("Case #%d: %d\n", Ti, Ans);
    }

}
