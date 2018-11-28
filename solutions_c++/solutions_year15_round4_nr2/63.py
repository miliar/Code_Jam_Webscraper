#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

#define EPS 1e-14L

using namespace std;

char res[1000];
int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        fprintf(stderr, "Z=%d\n", Z);
        int n; long double v, t;
        scanf("%d %Lf %Lf", &n, &v, &t);
        vector<long double> r(n), x(n);
        FO(i,0,n) scanf("%Lf %Lf", &r[i], &x[i]);
        FO(i,0,n) x[i] = x[i] - t;
        FO(i,0,n) FO(j,0,n) if (i < j && x[i] > x[j]) {
            swap(x[i],x[j]);
            swap(r[i],r[j]);
        }
        t = 1e100;
        long double s = 0, e = 1e8, b = -1;
        while ((e-s) > EPS && s*(1+EPS) < e) {
            long double m = (e+s)/2;
            long double mint = 0, maxt = -0;
            long double cv = 0;
            FO(i,0,n) {
                long double amt = min(m*r[i], v-cv);
                mint += x[i] * amt;
                cv += amt;
            }
            if (fabs(cv-v) < EPS) {
                cv = 0;
                for (int i = n-1; i >= 0; i--) {
                    long double amt = min(m*r[i], v-cv);
                    maxt += x[i] * amt;
                    cv += amt;
                }
                if (fabs(cv-v) < EPS) {
                    if (mint < EPS && maxt > -EPS) goto yes;
                    else goto no;
                } else goto no;
            } else goto no;

yes:;
    b = m;
    e = m;
    continue;
no:;
   s = m;
        }
        if (b > -0.5) printf("Case #%d: %.10Lf\n", Z, b);
        else printf("Case #%d: IMPOSSIBLE\n", Z);
    }
}

