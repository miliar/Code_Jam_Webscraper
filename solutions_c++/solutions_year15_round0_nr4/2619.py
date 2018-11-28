//Ominous Omino

#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, A, B, C;
const char Ans[2][10] = {"GABRIEL", "RICHARD"};
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d\n", &T);
    for (int Ts = 1; Ts <= T; Ts++)
    {
        scanf("%d %d %d", &A, &B, &C);
        int x = 1;
        if (A == 1) x = 0;
        if (A == 2 && B * C % 2 == 0) x = 0;
        if (A == 3 && B * C % 3 == 0 && B * C != 3) x = 0;
        if (A == 4 && (B * C == 12 || B * C == 16)) x = 0;
        printf("Case #%d: %s\n", Ts, Ans[x]);
    }
    return 0;
}
