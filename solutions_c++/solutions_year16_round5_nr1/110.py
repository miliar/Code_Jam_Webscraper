#include <cstdio>
#include <cstring>
#include <stack>
using namespace std;

int n;
char s[1 << 20];
char st[1 << 20];
int stop;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%s", s);
        n = strlen(s);
        stop = 0;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (stop > 0 && st[stop - 1] == s[i]) {
                ans += 10;
                --stop;
            } else {
                st[stop++] = s[i];
            }
        }
        if (stop % 2 == 1) {
            ans += ((stop - 1) / 2) * 10;
        } else {
            ans += (stop / 2) * 5;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
