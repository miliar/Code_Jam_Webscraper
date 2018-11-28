#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

#define N 1005
#define eps 1e-8

int n;
int a[N], b[N];

int solve1() {
    set < int > st;
    for (int i = 0; i < n; ++i)
        st.insert(a[i]);
    sort(b, b + n);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        auto it = st.upper_bound(b[i]);
        if (it != st.end()) {
            ++cnt;
            st.erase(it);
        }
    }
    return cnt;
}

int solve2() {
    set < int > st;
    for (int i = 0; i < n; ++i)
        st.insert(b[i]);
    sort(a, a + n);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        auto it = st.upper_bound(a[i]);
        if (it != st.end()) {
            ++cnt;
            st.erase(it);
        }
    }
    return n - cnt;
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int ci = 1; ci <= cas; ++ci) {
        double x;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &x);
            a[i] = int(x * 100000 + eps);
        }
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &x);
            b[i] = int(x * 100000 + eps);
        }
        printf("Case #%d: %d %d\n", ci, solve1(), solve2());
    }
    return 0;
}
