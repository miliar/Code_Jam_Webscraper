#include <cstdio>
#include <vector>
#include <set>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int re = 1; re <= T; ++re) {
        int n, x;
        scanf("%d%d", &n, &x);
        multiset<int> s;
        for (int i = 0; i < n; ++i) {
            int a;
            scanf("%d", &a);
            s.insert(a);
        }
        int ans = 0;
        while (!s.empty()) {
            ++ans;
            int a = *s.rbegin();
            auto it = s.end();
            it--;
            s.erase(it);
            int b = x - a;
            if (s.empty()) {
                break;
            }
            it = s.upper_bound(b);
            if (it != s.begin()) {
                --it;
                s.erase(it);
            }
        }
        printf("Case #%d: %d\n", re, ans);
    }
    return 0;
}