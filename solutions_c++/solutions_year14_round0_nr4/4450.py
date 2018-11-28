#include <cstdio>
#include <cstring>
#include <algorithm> 

static const int N = 1000;
int main() {
    using namespace std;
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        scanf("%d", &n);
        double a[N], b[N];
        bool used[N];
        for (int j = 0; j < n; ++j) 
            scanf("%lf", &a[j]);
        for (int j = 0; j < n; ++j) 
            scanf("%lf", &b[j]);
        memset(used, 0, n);
        std::sort(a, a + n);
        std::sort(b, b + n);
        int score0 = 0, score1 = 0;
        for (int j = 0, k = 0; j < n; ++j) {
            if (a[j] > b[k]) {
                ++score0;
                ++k;
            }
        }
        int min_k = 0;
        for (int j = 0; j < n; ++j) {
            bool more = true;
            for (int k = min_k; k < n; ++k) {
                if (!used[k] && b[k] > a[j]) {
                    used[k] = true;
                    more = false;
                    break;
                }
            }
            if (more) {
                while(used[min_k])
                    ++min_k;
                used[min_k] = true;
                ++score1;
            }
        }
        printf("Case #%d: %d %d\n", i + 1, score0, score1);
    }
    return 0;
}
