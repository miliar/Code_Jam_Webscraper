#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>

#define MAX 1024

using namespace std;

double a[MAX], b[MAX];
set<double> st;

int calc1(int n) {
    int i, j, ret = 0;

    for (i = j = 0; i < n; ++i) {
        if (a[i] > b[j]) {
            ++ret; ++j;
        }
    }

    return ret;
}

int calc2(int n) {
    int i, ret = 0;
    set<double>::iterator it;

    st.clear();
    for (i = 0; i < n; ++i) st.insert(b[i]);
    for (i = 0; i < n; ++i) {
        it = st.lower_bound(a[i]);
        if (it == st.end()) {
            ++ret; st.erase(st.begin());
        } else {
            st.erase(it);
        }
    }

    return ret;
}

int main() {
    int t, ct = 0, n, i;

    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; ++i) scanf("%lf", &a[i]);
        for (i = 0; i < n; ++i) scanf("%lf", &b[i]);
        sort(a, a + n);
        sort(b, b + n);
        printf("Case #%d: %d %d\n", ++ct, calc1(n), calc2(n));
    }

    return 0;
}
