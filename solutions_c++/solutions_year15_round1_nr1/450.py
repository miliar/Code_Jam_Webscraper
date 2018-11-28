#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX 1005

int n, a[MAX];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        int ans1 = 0;
        for (int i = 1; i < n; i++)
            if (a[i] < a[i-1])
                ans1 += a[i-1] - a[i];
        int ans2 = 0, rate = 0;
        for (int i = 1; i < n; i++)
            rate = max(rate, max(0, a[i-1] - a[i]));
        for (int i = 1; i < n; i++)
            ans2 += min(rate, a[i-1]);
        printf("Case #%d: %d %d\n", t, ans1, ans2);
    }
}
