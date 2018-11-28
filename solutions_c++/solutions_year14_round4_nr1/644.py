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

bool gone[10005];

int main() {
    int t, tt;
    scanf("%d", &tt);
    for (t = 1; t <= tt; ++ t) {
        printf("Case #%d: ", t);

        int n, m;
        scanf("%d %d", &n, &m);
        vector<int> a;

        for (int i = 0; i < n; ++ i) {
            int b;
            scanf("%d", &b);
            a.push_back(b);
        }
        memset(gone, 0, sizeof(gone));
        sort(a.begin(), a.end());
        int ans = 0;
        for (int i = n - 1; i >= 0; -- i) if (!gone[i]) {
            int j = i - 1;
            while (j >= 0 && (gone[j] || a[i] + a[j] > m)) {
                -- j;
            }
            if (j >= 0) {
                gone[j] = 1;
            }
            gone[i] = 1;
            ++ ans;
        }

        printf("%d\n", ans);
    }
    return 0;
}
