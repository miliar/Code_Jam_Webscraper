#include <cstdio>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int x = 1; x <= T; x++)
    {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double tmp = 0.0, rate = 2.0, ans = X / rate, cnt;
        while (true)
        {
            tmp += C / rate;
            rate += F;
            cnt = tmp + X / rate;
            if (cnt < ans)
                ans = cnt;
            else
                break;
        }
        printf("Case #%d: %.7f\n", x, ans);
    }
    return 0;
}
