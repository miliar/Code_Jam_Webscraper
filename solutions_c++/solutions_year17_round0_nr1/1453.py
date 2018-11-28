#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char buf[2000];
int k;
int s;

void solve()
{
    int ans = 0;
    scanf("%s %d", buf, &k);
    s = strlen(buf);
    for (int i = 0; i + k <= s; ++i) {
        if (buf[i] == '-') {
            ans += 1;
            for (int j = 0; j < k; ++j)
                buf[i + j] = '+' + '-' - buf[i + j];
        }
    }
    for (int i = 0; i < s; ++i) {
        if (buf[i] != '+') {
            printf("IMPOSSIBLE");
            return;
        }
    }
    printf("%d", ans);
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}
