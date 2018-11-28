#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

const int N = 10;
int n, a[N], c[N];
const char s[] = "PRS";

string dfs(int i, int win) {

    if (i == 0) {
        c[win]++;
        return string() + s[win];
    } 
    string ans1 = dfs(i - 1, win);
    string ans2 = dfs(i - 1, (win + 1) % 3);
    return min(ans1 + ans2, ans2 + ans1);
}

int main() 
{
    freopen("A-large-.in","r",stdin);
    freopen("A-large-.out","w",stdout);
    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        scanf("%d%d%d%d", &n, &a[1], &a[0], &a[2]);
        string ans = "";
        for (int win = 0; win < 3; win++) {
            bool flag = true;
            memset(c, 0, sizeof(c));
            string ans_t = dfs(n, win);
            for (int i = 0; i < 3; i++) {
                if (c[i] != a[i]) {
                    flag = false;
                }
            }
            if (flag) {
                if (ans == "" || ans_t < ans) ans = ans_t;
            }
        }
        if (ans == "") ans = "IMPOSSIBLE";
        printf("Case #%d: ", cas);
        cout << ans << endl;
    }
    return 0;
}

