#include <cstdio>
#include <cstdlib>
#include <cstring>

#define N 1010

using namespace std;

int smax, s[N];
char st[N];
int sum, ans, len;

int main() {
    int cases;
    scanf("%d", &cases);
    for (int c = 1; c <= cases; c++) {
        scanf("%d%s", &smax, st);
        len = (int)strlen(st);
        for (int i = 0; i <= len; i++) {
            s[i] = st[i] - '0';
        }
        sum = s[0];
        ans = 0;
        for (int i = 1; i <= len; i++) {
            if (sum < i) {
                ans += i - sum;
                sum = i;
            }
            sum += s[i];
        }
        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}
