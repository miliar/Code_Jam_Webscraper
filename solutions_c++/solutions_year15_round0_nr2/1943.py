#include <cstdio>
#include <set>
#include <cmath>

using namespace std;

int N;

int f(int level, multiset<int> st) {
    int x,y;
    int cnt = 0;
    while (!st.empty() and *st.rbegin() > level) {
        x = *st.rbegin();st.erase(--st.end());
        y = x - level;
        if (y > level) {
            st.insert(y);
        }
        cnt++;
    }

    int ans = level + cnt;
    //printf("%d: %d\n", level, ans);

    return ans;
}

int solve() {
    scanf("%d", &N);
    multiset<int> st;
    int x;
    int mx = 0;
    for (int i = 1; i <= N; i++) {
        scanf("%d", &x);
        st.insert(x);
        mx = max(x, mx);
    }

    int tmp;
    int ans = mx;
    for (int i = mx - 1; i >= 1; i--) {
        tmp = f(i, multiset<int>(st.begin(), st.end()));

        if (tmp < ans) {
            ans = tmp;
        }
    }

    return ans;
}

int main() {
    int NC;
    scanf("%d", &NC);
    for (int i=1; i <= NC; i++) {
        int ans = solve();
        printf("Case #%d: %d\n", i, ans);
    }
}