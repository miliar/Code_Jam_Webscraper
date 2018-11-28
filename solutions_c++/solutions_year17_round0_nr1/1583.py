#include<bits/stdc++.h>
using namespace std;

const int Len = 1010;
char str[Len];
int num;

int main() {
    freopen("A2.in", "r", stdin);
    freopen("A2.out", "w", stdout);
    int T;
    bool flag;
    int ans;
    scanf("%d\n", &T);
    for (int _cas = 1; _cas <= T; _cas++) {
        scanf("%s %d", str, &num);
        int l = strlen(str);
        flag = true;
        ans = 0;
        for (int i = 0; i < l; i++)
            str[i] = str[i] == '+';
        for (int i = 0; i < l; i++) {
            if (!str[i]) {
                if (i + num - 1 >= l) {
                    flag = false;
                    break;
                }
                else {
                    ans++;
                    for (int j = i; j <= i+num-1; j++)
                        str[j] ^= 1;
                }
            }
        }
        printf("Case #%d: ", _cas);
        if (flag) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
