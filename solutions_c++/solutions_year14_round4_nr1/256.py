#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, m;
        scanf("%d%d", &n, &m);
        multiset<int> ss;
        multiset<int> :: iterator pos;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            ss.insert(x);
        }
        int tot = 0;
        while (ss.size() != 0) {
            tot++;
            pos = ss.end();
            pos--;
            int num = *pos;
            ss.erase(pos);
            pos = ss.upper_bound(m - num);
            if (pos == ss.begin()) {
                continue;
            } else {
                pos--;
                ss.erase(pos);
            }
        }
        printf("Case #%d: %d\n", cas, tot);
    }
    return 0;
}
