#include <cstdio>
#include <cstring>
using namespace std;

#define MAXL 110

bool isconsoant(char c) {
    if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')
        return 1;
    return 0;
}

int main() {
    int T, n;
    char str[MAXL];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s %d", str, &n);
        int len = strlen(str);
        int ans = 0;
        for (int i = 0; i < len; i++) {
            for (int j = i+n-1; j < len; j++) {
                int cnt = 0;
                for (int k = i; k <= j; k++) {
                    if (isconsoant(str[k]))
                        cnt++;
                    else if (cnt >= n)
                        break;
                    else
                        cnt = 0;
                }
                if (cnt >= n)
                    ans++;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
