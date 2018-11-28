#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, j, k;
        double v, x, l, r, m;
        vector <pair<double, double> > w;
        
        scanf("%d %lf %lf", &n, &v, &x);
        
        for (j = 0; j < n; j++) {
            double p, q;
            
            scanf("%lf %lf", &p, &q);
            
            w.push_back(make_pair(q, p));
        }
        
        sort(w.begin(), w.end());
        
        if (w[0].first > x || w.back().first < x) {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
            
            continue;
        }
        
        l = 0, r = 1e9, m = (l + r) / 2;
        
        for (j = 0; j < 100; j++) {
            double v1 = 0, x1 = 0, v2 = 0, x2 = 0;
            
            for (k = 0; k < w.size(); k++) {
                double v0 = w[k].second * m;
                double x0 = w[k].first;
                
                if (v1 + v0 >= v) {
                    v0 = v - v1;
                    x1 = (v0 * x0 + v1 * x1) / (v0 + v1);
                    v1 = v;
                    
                    break;
                } else {
                    x1 = (v0 * x0 + v1 * x1) / (v0 + v1);
                    v1 += v0;
                }
            }
            
            for (k = w.size() - 1; k >= 0; k--) {
                double v0 = w[k].second * m;
                double x0 = w[k].first;
                
                if (v2 + v0 >= v) {
                    v0 = v - v2;
                    x2 = (v0 * x0 + v2 * x2) / (v0 + v2);
                    v2 = v;
                    
                    break;
                } else {
                    x2 = (v0 * x0 + v2 * x2) / (v0 + v2);
                    v2 += v0;
                }
            }
            
            if (v1 < v || x1 > x || x2 < x) {
                l = m;
                m = (l + r) / 2;
            } else {
                r = m;
                m = (l + r) / 2;
            }
        }
        
        printf("Case #%d: %.12lf\n", i + 1, r);
    }
    
    return 0;
}
