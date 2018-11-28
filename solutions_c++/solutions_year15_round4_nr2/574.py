# include <iostream>
# include <cstdio>
# include <cstring>
# include <vector>
# include <algorithm>

using namespace std;

const int MAXN = 100 + 10;
typedef pair<double,double> pdd;
double tx, ty, x, y;

bool cmp(const pdd&a,const pdd&b) {
    return a.second < b.second;
}

double solve(pdd a,pdd b,double s) {
    a.second = ty - a.second;
    b.second = b.second - ty;
    double u = a.first * a.second;
    double v = b.first * b.second;
    double all;
    if(u > v) {
        all = a.first * v / u + b.first + s;
    } else {
        all = a.first + b.first * u / v + s;
    }
    return tx / all;
}

int main() {
    freopen("b.in","r",stdin);
    int T, cas = 0, n; scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d%lf%lf", &n, &tx, &ty);
        double sumr = 0, ans = 1e30;
        vector<pdd> sm, lg;
        for(int i = 0; i < n; ++i) {
            scanf("%lf%lf", &x, &y);
            if(y == ty) {
                sumr += x;
                continue;
            }
            if(y < ty) 
                sm.push_back(pdd(x,y));
            else 
                lg.push_back(pdd(x,y));
            sort(sm.begin(), sm.end(), cmp);
            reverse(sm.begin(), sm.end());
            sort(lg.begin(), lg.end(), cmp);
        }
        if(sumr) ans = tx / sumr;
        pdd smv(0,0);
        for(size_t i = 0; i < sm.size(); ++i) {
            smv.second = (smv.first * smv.second + sm[i].first * sm[i].second);
            smv.first += sm[i].first; smv.second = smv.second / smv.first;
            pdd lgv(0,0);
            for(size_t j = 0; j < lg.size(); ++j) {
                lgv.second = (lgv.first * lgv.second + lg[j].first * lg[j].second);
                lgv.first += lg[j].first; lgv.second = lgv.second / lgv.first;
                ans = min(ans, solve(smv, lgv, sumr));
            }
        }
        if(ans == 1e30) puts("IMPOSSIBLE");
        else printf("%.10lf\n", ans);
    }
    return 0;
}

