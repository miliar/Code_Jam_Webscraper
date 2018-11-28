#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <stdexcept>
#include <functional>
#include <iomanip>

using namespace std;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define BGN begin()
#define ED end()
#define SZ size()
#define SORT(p) sort(p.BGN,p.ED)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define eps 1e-8

double c, f, x;

double calc(int n) {
    double ff = 2;
    double ret = 0;
    for(int i = 0; i < n; i++) {
        ret += c / ff;
        ff += f;
    }
    ret += x / ff;
    return ret;
}

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int C = 1; C <= T; C++) {
        scanf("%lf%lf%lf", &c, &f, &x);
        int l = 0, r = (int)x + 1, ml, mr;
        while(r - l > 10) {
//            printf("l = %d r = %d\n", l, r);
            ml = l + (r - l) / 3;
            mr = r - (r - l) / 3;
            double tl = calc(ml);
            double tr = calc(mr);
            if(tl - tr > eps) {
                l = ml;
            }
            else {
                r = mr;
            }
        }
        double ans = 1e40;
        for(int m = l; m <= r; m++) {
            double t = calc(m);
            if(ans - t > eps) {
                ans = t;
            }
        }
        printf("Case #%d: %.7f\n", C, ans);
    }
    return 0;
}
