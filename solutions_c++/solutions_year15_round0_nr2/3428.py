#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

int n, m, ans, tmp;
int a[1100];

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int cas; cin >> cas;
    multiset<int>::iterator iter;
    for (int t = 1; t <= cas; t++) {
        cin >> n; ans = 0;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            ans = max(ans, a[i]);
        }
        for (int i = 1; i <= ans; i++) {
            m = i;
            for (int j = 0; j < n; j++) {
                if (a[j] <= i) continue;
                tmp = a[j] - i;
                if (tmp % i) ++m;
                m += tmp / i;
            }
            ans = min(ans, m);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
