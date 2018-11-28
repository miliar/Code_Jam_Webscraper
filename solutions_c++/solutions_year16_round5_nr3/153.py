#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

typedef double real;

void clear() {
}

struct P {
    real x, y, z;
};

const int maxn = 1005;
const real inf = 1e9;

int n, s;
P p[maxn], v[maxn];
bool seen[maxn];
real dist[maxn];

real sqr(real x) {
    return x*x;
}
real getdist(P a, P b) {
    return std::sqrt(sqr(a.x - b.x) + sqr(a.y - b.y) + sqr(a.z - b.z));
}

int main() {
    int testcases; scanf("%d", &testcases);
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d: ", testnum);
        scanf("%d%d", &n, &s);
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf%lf", &p[i].x, &p[i].y, &p[i].z);
            scanf("%lf%lf%lf", &v[i].x, &v[i].y, &v[i].z);
        }
        std::fill(seen, seen+n, false);
        std::fill(dist, dist+n, inf);
        dist[0] = 0;
        for (int i = 0; i < n; i++) {
            int k = 0;
            for (int j = 0; j < n; j++) if (!seen[j]) k = j;
            for (int j = 0; j < n; j++) if (!seen[j] && dist[j] < dist[k]) k = j;
            seen[k] = true;
            if (k == 1) break;
            for (int l = 0; l < n; l++) {
                domin(dist[l], std::max(dist[k], getdist(p[l], p[k])));
            }
        }
        printf("%.6lf\n", dist[1]);
        clear();
    }
}

