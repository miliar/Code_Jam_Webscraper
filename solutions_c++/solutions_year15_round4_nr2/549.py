#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define FORE(it,c) for(__typeof(c.begin())it=c.begin();it!=c.end();it++)
typedef pair<int,int> pii;
typedef pair<double, double> pdd;

const int maxN = 111;
const double eps = 1e-8;

int n, test;
pdd a[maxN];
double X, V;

void solve(){
    scanf("%d", &n);
    scanf("%lf%lf", &V, &X);
    for (int i = 0; i < n; i++){
        scanf("%lf%lf", &a[i].se, &a[i].fi);
    }
    //Merge
    sort(a, a + n);
    int m = 1;
    for (int i = 1; i < n; i++) if (abs(a[m-1].fi - a[i].fi) < eps){
        a[m-1].se += a[i].se;
    }
    else a[m++] = a[i];
    n = m;
    //Check if n = 1
    if (n == 1){
        if (abs(a[0].fi - X) < eps)
            printf("%.10lf\n", V / a[0].se);
        else printf("IMPOSSIBLE\n");
        return;
    }
    //Find result
    if (a[n-1].fi < X - eps || a[0].fi > X + eps){
        printf("IMPOSSIBLE\n");
        return;
    }
    //printf("n = 2 %.4lf, %.4lf, %.4lf ", X, a[0].fi, a[1].fi);
    //printf("n = 2 ");
    //if (abs(a[0].fi - X) < eps) printf("%.10lf ", V/a[0].se); else if (abs(a[1].fi - X) < eps) printf("%.10lf ", V/a[1].se);
    double res = -1.0, mint = 1.0;
    for (int k = 0; k < n; k++){
        //Find Tx
        double s = 0.0;
        for (int i = 0; i < n; i++)
            s += (a[i].fi - a[k].fi) * a[i].se;
        double t = (X - a[k].fi) * V / s;
        res = max(res, t);
        mint = min(res, t);
    }
    if (mint + eps < 0 || res + eps < 0) printf("IMPOSSIBLE\n");
    else{
        if (abs(res) < eps) res = 0.0;
        printf("%.10lf\n", res);
    }
}

int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t; scanf("%d", &t);
    for (test = 1; test <= t; test++){
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
