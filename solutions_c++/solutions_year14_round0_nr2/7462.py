#include <cstdio>
#include <iostream>

using namespace std;

double C, F, X, ans, nowF, nextL;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;

    for (int Cas = 1; Cas <= T; ++Cas)
    {
        printf("Case #%d: ", Cas);

        cin >> C >> F >> X;

        ans = nextL = 0;
        nowF = 2.0;

        while (1)
        {
            nextL = C / nowF;
            if (nextL + X / (nowF + F) < (X / nowF))
                ans += nextL, nowF += F;
            else
            {
                ans += X / nowF;
                break;
            }
        }

        printf("%.7f\n", ans);
    }

    return 0;
}
