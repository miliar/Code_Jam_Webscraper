#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1050;
#define sqr(x) ((x)*(x))
int N, TC, S, x[MAXN], y[MAXN], z[MAXN], vx[MAXN], vy[MAXN], vz[MAXN], p[MAXN];
int par(int a) {
    if (p[a] == a) return a;
    return p[a] = par(p[a]);
}
void merge (int a, int b) {
    a = par(a), b = par(b);
    p[a] = b;
}
long long dist(int a, int b) {
    return sqr(x[a] - x[b]) + sqr(y[a] - y[b]) + sqr(z[a] - z[b]);
}
vector<pair<long long, pair<int, int> > > v;
int main () {
    scanf("%d", &TC);
    for (int T = 1; T<= TC; ++T) {
        scanf("%d%d", &N, &S);
        v.clear();
        for (int i = 0; i < N; ++i) {
            scanf("%d%d%d%d%d%d", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
            p[i] = i;
            for (int j = 0; j < i; ++j) 
                v.push_back(make_pair(dist(i, j), make_pair(i, j)));
        }
        sort(v.begin(), v.end());
        for (auto it:v) {
            merge(it.second.first, it.second.second);
            if (par(0) == par(1)) {
                printf("Case #%d: %.9lf\n", T, sqrt(it.first));
                break;
            }
        }
    }
}