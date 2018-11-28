#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

const int MAXN = 1000 + 3;
char str[MAXN];
int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase) {
        int n;
        scanf("%d%s", &n, str);
        int cur = 0, ans = 0;
        for (int i = 0; i <= n; ++i) {
            int c = str[i] - '0';
            if (cur < i) {
                ans += i-cur;
                c += i-cur;
            }
            cur += c;
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}

