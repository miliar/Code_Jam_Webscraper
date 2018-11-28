#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;
const int maxn = 1111;
double a[maxn], b[maxn];
int main() {
    freopen("dl.in", "r", stdin);
    freopen("dl.out", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while(T--) {
        int n;
        int ans1 = 0, ans2 = 0;
        cin >> n;
        for (int i = 1; i <= n; ++i) cin >> a[i];
        for (int i = 1; i <= n; ++i) cin >> b[i];
        sort(a + 1, a + 1 + n);
        sort(b + 1, b + 1 + n);
        int p1 = 1, p2 = n;
        for (int i = n; i > 0; i--) {
            if (b[i] > a[p2]) {
              //  ans2++;
                p1++;
            } else if (b[i] < a[p2]) {
                ans1++;
                p2--;
            }
        }
        p1 = 1, p2 = n;
        int lose = 0;
        for (int i = 1; i <= n; ++i) {
            while (p1 <= n && b[p1] < a[i]) p1++;
            if (p1 > n) break;
            if (b[p1] > a[i]) lose++;
            p1++;
        }
        ans2 = n - lose;


        printf("Case #%d: %d %d\n", ++ca, ans1, ans2);
    }
    return 0;
}
