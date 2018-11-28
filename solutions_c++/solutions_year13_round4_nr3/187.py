#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
int a[2000], b[2000], c[2000];
set<int> x[2000], y[2000];
void solve() {
    int n;
    scanf("%d", &n);
    for (int i = 0 ; i < n ; ++i) scanf("%d", a + i);
    for (int i = 0 ; i < n ; ++i) scanf("%d", b + i);
    for (int i = 0 ; i < n ; ++i) c[i] = 0;
    for (int i = 0 ; i < n ; ++i) {
        for (int j = 0 ; j < n ; ++j) x[j].clear(), y[j].clear();
        x[0].insert(0);
        if (c[0]) x[0].insert(a[0]);
        y[n - 1].insert(0);
        if (c[n - 1]) y[n - 1].insert(b[n - 1]);
        for (int j = 1 ; j < n ; ++j) {
            x[j] = x[j - 1];
            if (c[j]) x[j].insert(a[j]);
        }
        for (int j = n - 2 ; j >= 0 ; --j) {
            y[j] = y[j + 1];
            if (c[j]) y[j].insert(b[j]);
        }
        //for (int j = 0 ; j < n ; ++j) printf(" %d", a[j]);
        //puts("");
        int k = -1;
        for (int j = 0 ; j < n ; ++j)
            if (!c[j] && x[j].find(a[j] - 1) != x[j].end() && y[j].find(b[j] - 1) != y[j].end()) {
                k = j;
                break;
            }
        c[k] = i + 1;
    }
    for (int i = 0 ; i < n ; ++i) printf(" %d", c[i]);
    printf("\n");
}
int main() {
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 1 ; i <= t ; ++i) {
        printf("Case #%d:", i);
        solve();
    }
    return 0;
}