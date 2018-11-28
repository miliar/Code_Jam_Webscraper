#include <cstdio>
#include <cstring>
using namespace std;

#define MAXN 10000000

bool ispal(char *str) {
    int i = 0, j = strlen(str)-1;
    while (i < j)
        if (str[i++] != str[j--])
            return 0;
    return 1;
}

int T, cnt;
char str[32];
long long A, B, a[MAXN];

int main() {
    cnt = 0;
    for (int i = 1; i <= MAXN; i++) {
        sprintf(str, "%d", i);
        if (ispal(str)) {
            long long j = (long long) i*i;
            sprintf(str, "%lld", j);
            if (ispal(str))
                a[cnt++] = j;
        }
    }

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld %lld", &A, &B);
        int ans = 0;
        for (int i = 0; i < cnt; i++)
            if (A <= a[i] && a[i] <= B)
                ans++;
        printf("Case #%d: %d\n", t, ans);
    }
}
