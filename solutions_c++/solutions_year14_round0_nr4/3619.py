#include <iostream>
#include <set>
#include <functional>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int N = 1111;
const double eps = 1e-10;
typedef set<int>::iterator sit;
int a[N], b[N], n;

int calc(int a[], int b[], int n) {
    int res = 0;
    set<int> s;
    for (int i = 0; i < n; i++) s.insert(b[i]);
    for (int i = 0; i < n; i++) {
        if (a[i] > *s.begin()) {
            res++;
            s.erase(s.begin());
        } else {
            sit it = s.end();
            it--;
            s.erase(it);
        }
    }
    return res;
}

void solve() {
    int ans1 = 0, ans2 = 0;
    set<int> s;
    sort(a, a + n);
    sort(b, b + n);
    for (int i = 0; i < n; i++) s.insert(b[i]);
    for (int i = 0; i < n; i++) {
        sit it = s.lower_bound(a[i]);
        if (it != s.end()) {
            s.erase(it);
        } else {
            s.erase(s.begin());
            ans2++;
        }
    }
    ans1 = ans2;
    for (int i = 0; i < n; i++) {
        ans1 = max(ans1, calc(a + i, b, n - i));
    }
    printf("%d %d\n", ans1, ans2);
}

int main() {
    freopen("p3l.in", "r", stdin);
    freopen("p3l.out", "w", stdout);
    int T, Case = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        double x;
        for (int i = 0; i < n; i++) { scanf("%lf", &x); a[i] = (int) ((x + eps) * 100000); }
        for (int i = 0; i < n; i++) { scanf("%lf", &x); b[i] = (int) ((x + eps) * 100000); }
        printf("Case #%d: ", Case++);
        solve();
    }
    return 0;
}
