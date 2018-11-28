#include <cstdio>
#include <algorithm>
#include <cstring>
#include <climits>
using namespace std;

const int kMaxN = 1000 + 10;
int D;
int T;
int p[kMaxN];

int main() {
    scanf("%d", &T);
    for (int c = 0; c < T; ++c) {
        scanf("%d", &D);
        int maxP = 0;
        for (int i = 0; i < D; ++i) {
            scanf("%d", &p[i]);
            maxP = max(maxP, p[i]);
        }
        int ans = INT_MAX;
        for (int i = 1; i <= maxP; ++i) {
            int sum = i;
            for (int j = 0; j < D; ++j) {
                sum += (p[j] + i - 1) / i - 1;
            }
            ans = min(ans, sum);
        }
        printf("Case #%d: %d\n", c + 1, ans);
    }
    return 0;
}
