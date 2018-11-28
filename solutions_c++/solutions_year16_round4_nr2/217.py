#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define FOR(i, x, y) for(int i = x; i < y; ++ i)
#define pb push_back
#define mk make_pair

const int N = 205;
int n,m;
double p[N];
double a[N];
double f[N];

double get(){
    int m1 = m / 2;
    FOR(i,0,m1 + 1) f[i] = 0;
    f[0] = 1;
    FOR(i,0,m){
        for (int j = m1; j > 0; --j)
            f[j] = f[j-1] * a[i] + f[j] * (1 - a[i]);
        f[0] *= (1 - a[i]);
    }
    return f[m1];
}

void solve() {
    scanf("%d%d",&n, &m);
    FOR(i,0,n)
        scanf("%lf", p+i);
    double ans = 0;
    sort(p, p + n);
    FOR(c,0,m+1){
        int k = 0;
        FOR(i,0,c) a[k++] = p[i];
        FOR(i,0,m-c)
            a[k++] = p[n-1-i];
        ans = max(ans, get());
    }
    printf("%.9lf\n", ans);
}


int main() {
#ifdef LOCAL
    freopen("in","r",stdin);
#endif
    int T, Case = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++Case);
        solve();
    }
    return 0;
}
