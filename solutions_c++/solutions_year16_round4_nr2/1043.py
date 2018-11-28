#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
double p[105];
int main() {
    freopen("in.in", "r", stdin);
    freopen("check.out", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while(T--) {
        int n, K;
        scanf("%d%d", &n, &K);
        for(int j = 0; j < n; j++) scanf("%lf", &p[j]);
        double ans = 0;
        for(int i = 0; i < 1 << n; ++i) {
            if(__builtin_popcount(i) != K) continue;
            double tmp = 0;
            for(int j = i; j; j = (j - 1) & i) {
                if(__builtin_popcount(j) != K / 2) continue;
                double cur = 1;
                for(int k = 0; k < n; ++k) {
                    if(j >> k & 1) cur *= p[k];
                    else if(i >> k & 1) cur *= (1 - p[k]);
                }
                tmp += cur;
            }
            ans = max(ans, tmp);
        }
        printf("Case #%d: %f\n", cas++, ans);
    }
    return 0;
}
