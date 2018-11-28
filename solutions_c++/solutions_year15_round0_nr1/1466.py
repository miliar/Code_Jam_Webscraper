#include <bits/stdc++.h>
using namespace std;

int nTest;
int s_max, need, total;
char s[1010];

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A_out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {
        scanf("%d%s", &s_max, s);
        total = 0;
        need = 0;
        for (int i = 0; i <= s_max; i++) {
            s[i] -= '0';
            if (!s[i]) continue;
            while (total < i) {
                total++;
                need++;
            }
            total += s[i];
        }
        printf("Case #%d: %d\n", test, need);
    }

    return 0;
}