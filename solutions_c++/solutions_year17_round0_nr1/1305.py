#include <stdio.h>
#include <string.h>
using namespace std;

int Work(char s[], int k, int len) {
    int ans = 0;
    for (int i = 0; i <= len - k; i++) {
        if (s[i] == '-') {
            for (int j = 0; j < k; j++) {
                if (s[i + j] == '-') {
                    s[i + j] = '+';
                } else {
                    s[i + j] = '-';
                }
            }
            ans++;
        }
    }
    for (int i = 0; i < len; i++) {
        if (s[i] == '-') {
            return -1;
        }
    }
    return ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        char s[10000];
        int k;
        scanf("%s%d", s, &k);
        int ans = Work(s, k, strlen(s));
        printf("Case #%d: ", t);
        if (ans < 0) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
