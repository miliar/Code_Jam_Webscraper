#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <queue>
using namespace std;

void solve()
{
    int n, j;
    scanf("%d%d", &n, &j);
    for (long long x = (1LL << n - 1) + 1; x < 1LL << n && j > 0; ++ x) {
        if (!(x & 1)) {
            continue;
        }
        bool valid = true;
        vector<long long> ret;
        for (int base = 2; base <= 10 && valid; ++ base) {
            long long value = 0, power = 1;
            for (int i = 0; i < n; ++ i) {
                if (x >> i & 1) {
                    value += power;
                }
                power *= base;
            }
            long long opt = -1;
            for (long long div = 2; div * div <= value; ++ div) {
                if (value % div == 0) {
                    opt = div;
                    break;
                }
            }
            if (opt == -1) {
                valid = false;
            } else {
                ret.push_back(opt);
            }
        }
        if (valid) {
            bool first = true;
            for (int i = 0; i < n; ++ i) {
                if (first && (x >> (n - 1 - i) & 1) == 0) {
                    continue;
                }
                first = false;
                printf("%d", x >> (n - 1 - i) & 1);
            }
            for (int i = 0; i < ret.size(); ++ i) {
                printf(" %I64d", ret[i]);
            }
            puts("");
            -- j;
        }
    }
}

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        printf("Case #%d:\n", test);
        solve();
    }
    return 0;
}
