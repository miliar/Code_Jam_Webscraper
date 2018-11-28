#include <cstdio>
#include <algorithm>
#define infile "b.in"
#define outfile "b.out"

using namespace std;

double c, f, x;
double res;

void solve() {

    res = x / 2;
    double s = 0;

    for (int i = 1; i <= x; ++i) {
        s += c / (2 + (i-1)*f);
        res = min(res, s + x / (2 + i*f));
    }

}

void write(int t) {
    printf("Case #%d: %.7lf\n", t, res);
}

int main() {
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);

    int t;
    scanf("%d\n", &t);

    for (int i = 0; i < t; ++i) {
        scanf("%lf %lf %lf\n", &c, &f, &x);
        solve();
        write(i+1);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
