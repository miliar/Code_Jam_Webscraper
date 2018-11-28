#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

const int N = 15;

pair<int, int> p[N];
int k;

int check(int m1, int m2, int d2) {
    int res = m2 / m1;
    double a = (m2 + 0.0) / (m1 + 0.0) - res;
    a *= 360;
    if(d2 + a > 360 + 1e-8) res++;
    return res;
}

int cal(int m1) {
    int res = 0;
    for(int i = 0; i < k; i++) {
        res += check(m1, p[i].second, p[i].first);
    }
    return res;
}

int main() {
    freopen("C-small-1-attempt3.in", "r", stdin);
    freopen("C-small-1-attempt3.out", "w", stdout);
    int _, cnt = 0;
    scanf("%d", &_);
    while(_--) {
        int n;
        k = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            int h, d, m;
            scanf("%d%d%d", &d, &h, &m);
            for(int j = 0; j < h; j++) p[k].first = d, p[k++].second = m;
        }
        if(k == 1) { printf("Case #%d: 0\n", ++cnt); continue; }
        if(p[0].second == p[1].second) { printf("Case #%d: 0\n", ++cnt); continue; }
        //if(p[0].first > p[1].first) swap(p[0], p[1]);
        if(p[0].second < p[1].second) swap(p[0], p[1]);
        if(p[0] == p[1]) { printf("Case #%d: 0\n", ++cnt); continue; }
        double t1 = 0, t2 = 0;
        t1 = (360.0 - p[0].first) / 360.0 * p[0].second;
        t2 = (360.0 - p[1].first) / 360.0 * p[1].second + p[1].second;
        if(t1 < t2 - 1e-8) { printf("Case #%d: 0\n", ++cnt); continue; }

        printf("Case #%d: 1\n", ++cnt); continue;
    }

    return 0;
}
