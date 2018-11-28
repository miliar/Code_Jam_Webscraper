#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define N 110

bool a[N];
char s[N];

void filp(int l, int r) {
    for (int i = l;i < r;i++) a[i] ^= 1;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, n, i, j, ca = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%s", s);
        n = strlen(s);
        for (i = 0;i < n;i++) {
            a[i] = (s[i]=='+');
        }
        int ans = 0;
        for (i = n-1;i >= 0;i--) {
            if (!a[i]) ans++, filp(0, i);
        }
        printf("Case #%d: %d\n", ca++, ans);
    }
}
