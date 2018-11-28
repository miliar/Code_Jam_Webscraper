#include <bits/stdc++.h>
#define sz(x) ((int)((x).size()))
typedef long long ll;

int N, V, X;
int r[105], c[105];

void f(int &a) { int b, c; scanf("%d.%d", &b, &c); a = 10000*b+c; }

int main()
{
    int TC; scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        scanf("%d", &N); f(V); f(X);
        for (int i = 0; i < N; i++) { f(r[i]); f(c[i]); }
        if (N == 1) {
            printf("Case #%d: ", tc);
            if (c[0] != X) printf("IMPOSSIBLE\n");
            else printf("%.8lf\n", double(V)/r[0]);
        } else if (N == 2) {
            bool pos = true; double ans = -1.;
            if ((c[0] < X && c[1] < X) || (c[0] > X && c[1] > X)) pos = false;
            else if (c[0] == X || c[1] == X) ans = (double(V) / ((c[0] == X ? r[0] : 0) + (c[1] == X ? r[1] : 0)));
            else {
                if (c[0] > c[1]) { std::swap(c[0], c[1]); std::swap(r[0], r[1]); }
                c[0] -= X; c[1] -= X;
                c[0] = -c[0];
                double tr = (r[0] + (r[1] * (double(r[0])*c[0]/c[1]/r[1]))) / std::max(1.0, (double(c[0])*r[0]/c[1]/r[1]));
                //printf("HI %d: %lf %d %d\n", tc, tr, c[0], c[1]);
                ans = V / tr;
            }
            printf("Case #%d: ", tc);
            if (pos) printf("%.8lf\n", ans);
            else printf("IMPOSSIBLE\n");
        }
    }
}

