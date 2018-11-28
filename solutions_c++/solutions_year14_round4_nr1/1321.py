#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

#define N 10005

int n, m;
int a[N];

int solve() {
    multiset < int > st;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
        st.insert(a[i]);
    }
    int cnt = 0;
    while (!st.empty()) {
        ++cnt;
        auto it = st.lower_bound(*st.rbegin());
        st.erase(it);
        if (st.empty()) break;
        auto jt = st.upper_bound(m - *it);
        if (jt != st.begin()) {
            --jt;
            st.erase(jt);
        }
        //printf("%d %d %d\n", cnt, *it, *jt);
    }
    return cnt;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--)
        printf("Case #%d: %d\n", ++cas, solve());
    return 0;
}
