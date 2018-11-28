#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int factor(const vector<int> &n, int base) {
    for (int d = 3; d < 100; d += 2) {
        int r = 0;
        for (int k = 0, p = 1; k < n.size(); k++, p = p * base % d)
            if (n[k])
                r = r + p;
        if (r % d == 0)
            return d;
    }
    return 0;
}

int main() {
    int T, n, m;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        printf("Case #%d:\n", t);
        for (long long mask = (1LL << (n-1)) + 1; mask < (1LL << n) && m > 0; mask += 2) {
            vector<int> d(n);
            for (int k = 0; k < n; k++)
                d[k] = (mask >> k) & 1;
            bool fail = false;
            vector<int> p;
            for (int b = 2; !fail && b <= 10; b++) {
                int f = factor(d, b);
                if (f > 0)
                    p.push_back(f);
                else
                    fail = true;
            }
            if (!fail) {
                char s[40];
                for (int k = 0; k < n; k++)
                    s[k] = d[n-1-k] + '0';
                s[n] = 0;
                printf("%s", s);
                for (int i = 0; i < 9; i++)
                    printf(" %d", p[i]);
                puts("");
                m--;
            }
        }
    }
}
