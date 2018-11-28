#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int kMaxN = 1000 + 10;
char s[kMaxN];
int sMax;

int main() {
    int cas;
    scanf("%d", &cas);
    for (int c = 0; c < cas; ++c) {
        scanf("%d%s", &sMax, s);
        int ans = 0;
        int sum = 0;
        for (int i = 0; i < sMax + 1; ++i) {
            int number = static_cast<int>(s[i] - '0');
            if (i > sum) {
                ans += i - sum;
                sum = i;
            }
            sum += number;
        }
        printf("Case #%d: %d\n", c + 1, ans);
    }
    return 0;
}
