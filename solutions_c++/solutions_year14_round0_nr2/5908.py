#include <iostream>
#include <iomanip>
#include <cstdio>
#define L(fmt, ...) do {if(false) printf(fmt "\n", ##__VA_ARGS__);}while(false)
using namespace std;
double C, F, X, v;

int main() {
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out", "w", stdout);
    ios::sync_with_stdio(false);
    int T, tn;
    double res, t1, t2;
    cin>>T;
    for (tn = 1; tn <= T; ++tn) {
        cin>>C>>F>>X;
        v = 2.0;
        res = 0;
        t1 = X/v; L("t1:%lf = %lf/%lf;", t1, X, v);
        t2 = C/v + X / (v + F); L("t2:%lf = %lf/%lf + %lf/(%lf + %lf);",
                                  t2, C, v, X, v, F);

        while (t2 <= t1) {
            res += C/v;
            v += F;
            t1 = X/v;L("t1:%lf = %lf/%lf;", t1, X, v);
            t2 = C/v + X / (v + F);L("t2:%lf = %lf/%lf + %lf/(%lf + %lf);",
                                  t2, C, v, X, v, F);
        }
        res += t1;
        cout<<"Case #"<<tn<<": ";
        cout<<fixed<<setprecision(7)<<res<<endl;

    }
    return 0;
}
