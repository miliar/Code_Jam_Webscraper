#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int t, tt;
    scanf("%d", &tt);
    for (t = 1; t <= tt; ++ t) {
        printf("Case #%d: ", t);

        int n;
        scanf("%d", &n);
        vector<int> v;
        for (int i = 0; i < n; ++ i) {
            int b; scanf("%d", &b);
            v.push_back(b);
        }

        int ans = 0;
        for (int i = 0; i < n; ++ i) {
            int left = 0, right = 0;
            for (int j = 0; j < n; ++ j) {
                if (v[j] > v[i]) {
                    if (j < i) ++ left;
                    else ++ right;
                }
            }
            ans += min(left, right);
        }

        printf("%d\n", ans);
    }
    return 0;
}
