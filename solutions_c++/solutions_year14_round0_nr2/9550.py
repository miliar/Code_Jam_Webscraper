#include <cstring>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

#define debug 01
#define openfile {freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}

const double eps = 0.0000001;

int t;
double x, f, c;

bool nhohonbang(double x, double y) {
    if (x-y <= eps) return(1);
    return(0);
}

void solve() {
    double res = 2000000000, sec = 0;
    double v = 2;
    if (nhohonbang(x,c)) {
        printf("%.7lf\n",x/2);
        return;
    }
    while (1) {
        sec += c/v;
        if (nhohonbang(res,sec+(x-c)/v)) {
            printf("%.7lf\n",res);
            return;
        }
        res = sec+(x-c)/v;
        v += f;
    }
}

int main() {
    if (debug) openfile;
    scanf("%d",&t);
    for (int te = 1; te <= t; ++te) {
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: ",te);
        solve();
    }
}
