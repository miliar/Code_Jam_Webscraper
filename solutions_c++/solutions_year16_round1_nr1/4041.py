#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;

const int maxn = 10005;
const int charSize = 26;
char str[maxn];
int g[2050][charSize], cnt[maxn];

void init(int len) {
    for (int i = 0; i < charSize; i++) {
        g[0][i] = -1;
    }

    for (int i = 1; i <= len; i++) {
        for (int j = 0; j < charSize; j++)
            g[i][j] = g[i - 1][j];
        g[i][str[i] - 'A'] = i;
    }
}


int main() {
#ifdef LOCAL
    freopen("/Users/yew1eb/ClionProjects/CppGo/in.txt", "r", stdin);
    freopen("/Users/yew1eb/ClionProjects/CppGo/out.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%s", str + 1);
        printf("Case #%d: ", cas);
        int len = strlen(str + 1);
        init(len);
        string ans = "";
        memset(cnt, 0, sizeof(cnt));
        for (int i = len; i >= 1; i--) {
            int ch = str[i] - 'A';
            if (i > 1) {
                for (int j = charSize-1; j >= 0; j--)
                    if (g[i - 1][j] != -1) {
                        ch = max(ch, j);
                        break;
                    }
            }
            if (ch == str[i] - 'A') {
                ans += str[i];
                cnt[i] = 1;
            }
        }

        for (int i = 1; i <= len; i++) {
            if (!cnt[i])
                ans += str[i];
        }
        printf("%s\n", ans.c_str());
    }
    return 0;
}