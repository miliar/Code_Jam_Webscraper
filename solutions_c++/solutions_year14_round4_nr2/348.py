#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 1000;
int a[maxn];
int main() {
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int c = 0 ; c < t ; ++c) {
        int n, x = 0;
        scanf("%d", &n);
        int l = 0, r = n;
        for (int i = 0 ; i < n ; ++i) scanf("%d", a + i);
        for (int i = 0 ; i < n ; ++i) {
            int k = -1;
            for (int j = l ; j < r ; ++j) if (k == -1 || a[j] < a[k]) k = j;
            if (k - l + 1 < r - k) {
                for (int j = k ; j > l ; --j) swap(a[j], a[j - 1]), ++x;
                ++l;
            }
            else {
                for (int j = k ; j < r - 1 ; ++j) swap(a[j], a[j + 1]), ++x;
                --r;
            }
        }
        printf("Case #%d: %d\n", c + 1, x);
    }
    return 0;
}