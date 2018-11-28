#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for (int z = 1; z <= t; z++) {
        int n;
        scanf("%d", &n);

        int a[n];
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int bigger[2] = {0, 0};

            for (int j = 0; j < n; j++)
                if (a[j] > a[i])
                    bigger[j > i]++;

            ans += min(bigger[0], bigger[1]);
        }

        printf("Case #%d: %d\n", z, ans);
    }
}
