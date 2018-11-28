#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAX 1000010

char str[MAX];
int sz, n;
int tb[MAX];

int isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s %d", str, &n);
        sz = strlen(str);
        long long ans = 0;
        /*
        for (int i = 0; i < sz; i++) {
            for (int j = i; j < sz; j++) {
                tb[i] = !isVowel(str[i]) ? 1 : 0;
                if (tb[i] == n) {
                    ans++;
                    // for (int l = i; l <= j; l++)
                    //     putchar(str[l]);
                    // puts("");
                    continue;
                }
                for (int k = i+1; k <= j; k++) {
                    if (isVowel(str[k]))
                        tb[k] = 0;
                    else
                        tb[k] = tb[k-1] + 1;
                    if (tb[k] == n) {
                        ans++;
                        // for (int l = i; l <= j; l++)
                        //     putchar(str[l]);
                        // puts("");
                        break;
                    }
                }
            }
        }
        */
        int last = -1;
        tb[0] = !isVowel(str[0]) ? 1 : 0;
        if (tb[0] >= n) {
            ans += sz;
            last = 0;
        }
        for (int i = 1; i < sz; i++) {
            if (isVowel(str[i]))
                tb[i] = 0;
            else
                tb[i] = tb[i-1] + 1;
            if (tb[i] == n) {
                if (last != -1)
                    ans += (long long) (i-n+2 - (last-n+2)) * (sz-i);
                else
                    ans += (long long) (i-n+2) * (sz-i);
                last = i;
            }
            else if (tb[i] > n) {
                ans += (sz-i);
                last = i;
            }
        }
        printf("Case #%d: %lld\n", t, ans);
    }
}
