#include <cstdio>

using namespace std;

int main() {
    int T; scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        double f, c, x, g = 2.0, o = 0.0; scanf("%lf%lf%lf", &c, &f, &x);
        while (true) {
            double t1 = x / g, t2 = c / g + x / (g + f);
            if (t1 < t2) {
                printf("Case #%d: %.7f\n", t, t1 + o); break;
            }
            else {
                o += c / g; g += f;
            }
        }
    }

    return 0;
}
