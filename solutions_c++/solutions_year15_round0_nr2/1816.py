#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1005;
const int INF = 0x3f3f3f3f;

int t, d, p[N];

int main() {
    int cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &d);
        int ans = INF;
        for (int i = 0; i < d; i++) scanf("%d", &p[i]);
        for (int i = 1; i <= 1000; i++) {
            int tmp = i;
            for (int j = 0; j < d; j++) {
                tmp += p[j] / i - (p[j] % i == 0);
            }
            ans = min(tmp, ans);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
