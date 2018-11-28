#include <cstdio>
#include <cstring>
using namespace std;

void work() {
    char s[110];
    scanf("%s", s);
    int ans = 0;
    char last = s[0];
    for (int i = 1; s[i]; i++) {
        if (s[i] != s[i - 1])
            ans++;
        last = s[i];
    }
    if (last == '-')
        ans++;
    printf("%d\n", ans);
}

int main() {
    int T, C = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++C);
        work();
    }
    return 0;
}
