#include <cstdio>
#include <algorithm>
#define eps 1e-10
using namespace std;

int N;
double V, X;
struct S {
    double R, C;
    bool operator<(const S &x) const {
        return C < x.C;
    }
} a[100];
double E[100];

bool fne(double a, double b) {
    return a + eps < b || b + eps < a;
}

void solve() {
    scanf("%d%lf%lf", &N, &V, &X);
    for (int i = 0; i < N; i++)
        scanf("%lf%lf", &a[i].R, &a[i].C);
    sort(a, a + N);
    double sE = 0, sR = 0;
    bool larger = false, lower = false, equal = false;
    for (int i = 0; i < N; i++) {
        if (X - eps < a[i].C && a[i].C < X + eps) equal = true;
        else if (a[i].C < X) lower = true;
        else larger = true;
        E[i] = a[i].R * a[i].C;
        sE += E[i];
        sR += a[i].R;
    }
    if (!equal && (!larger || !lower)) {
        puts("IMPOSSIBLE");
        return;
    }
    double ans;
    if (X - eps < sE / sR && sE / sR < X + eps) {
        ans = V / (a[0].R + a[1].R);
    } else if (sE / sR < X) {
        //k*a[0].R*a[0].C + a[1].R*a[1].C == X * (k*a[0].R + a[1].R)
        double k = (a[1].R*a[1].C - X * a[1].R) / (X * a[0].R - a[0].R*a[0].C);
        ans = V / (k * a[0].R + a[1].R);
        for (int i = 0; i < N; i++)
            if ((sE - E[i]) < X * (sR - a[i].R) - eps) {
                sE -= E[i];
                sR -= a[i].R;
            } else {
                if (fne(sE, X * sR) && fne(E[i], X * a[i].R)) {
                    double k = (sE - X * sR) / (E[i] - X * a[i].R);
                    sE -= k * E[i];
                    sR -= k * a[i].R;
                }
                break;
            }
    } else {
        double k = (a[0].R*a[0].C - X * a[0].R) / (X * a[1].R - a[1].R*a[1].C);
        ans = V / (k * a[1].R + a[0].R);
        for (int i = N - 1; i >= 0; i--)
            if ((sE - E[i]) > X * (sR - a[i].R) + eps) {
                sE -= E[i];
                sR -= a[i].R;
            } else {
                if (fne(sE, X * sR) && fne(E[i], X * a[i].R)) {
                    double k = (sE - X * sR) / (E[i] - X * a[i].R);
                    sE -= k * E[i];
                    sR -= k * a[i].R;
                }
                break;
            }
    }
    if (N == 1)
      ans = V / a[0].R;
    printf("%.8lf\n", ans);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
        printf("Case #%d: ", i), solve();
}
