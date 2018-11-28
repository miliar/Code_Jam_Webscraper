#include<iostream>
#include<cstdio>
#include<cstring>
#define LL long long
using namespace std;

int T, K, C, S, kase = 0;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        cin >> K >> C >> S;
        if (S == K)
        {
            int i;
            LL n = 1;
            for (i = 1; i <= C - 1; i++)
                n *= K;
            printf("Case #%d:", ++kase);
            for (i = 1; i <= S; i++)
                printf(" %lld", 1 + (i - 1) * n);
            printf("\n");
        }
    }
    return 0;
    fclose(stdin);
    fclose(stdout);
}
