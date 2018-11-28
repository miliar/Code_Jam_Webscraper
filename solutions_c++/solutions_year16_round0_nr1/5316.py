#include <bits/stdc++.h>

using namespace std;

int main() {
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; ++t) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", t);
        }
        else {
            vector<bool> seen(10, false);
            bool seen_all = false;
            int orig_n = n;
            while (!seen_all) {
                int tmp = n;
                while (tmp != 0) {
                    int digit = tmp % 10;
                    seen[digit] = true;
                    tmp /= 10;
                }
                seen_all = true;
                for (int i = 0; i < 10 && seen_all; ++i) {
                    if (!seen[i]) {
                        seen_all = false;
                    }
                }
                n += orig_n;
            }
            printf("Case #%d: %d\n", t, n - orig_n);
        }
    }
    return 0;
}
