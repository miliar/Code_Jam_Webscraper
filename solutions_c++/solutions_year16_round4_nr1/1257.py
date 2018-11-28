#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int a[3];
string g[13][3];

string dfs(int n, int sel) {
    if (n == 0) {
        if (sel == 0) {
            g[0][sel] = "P";
        } else if (sel == 1){
            g[0][sel] = "R";
        } else {
            g[0][sel] = "S";
        }
        return g[0][sel];
    }
    if (g[n][sel] != "") {
        return g[n][sel];
    }
    string l1 = dfs(n - 1, sel);
    string l2 = dfs(n - 1, (sel + 1) % 3);
    if (l1 + l2 < l2 + l1) {
        g[n][sel] = l1 + l2;
    } else {
        g[n][sel] = l2 + l1;
    }
    return g[n][sel];
}

int main() {
    freopen("A-large.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int tt = 1; tt <= testcase; tt++) {
        string ans = "";
        int n, sr, sp, ss;
        scanf("%d%d%d%d", &n, &sr, &sp, &ss);
        bool exist = false;
        for (int i = 0; i < 3; i++) {
            string s = dfs(n, i);
            int wr = 0, wp = 0, ws = 0;
            for (int j = 0; j < s.size(); j++) {
                if (s[j] == 'P') {
                    wp++;
                }
                if (s[j] == 'R') {
                    wr++;
                }
                if (s[j] == 'S') {
                    ws++;
                }
            }
            // printf("%s\n", s.c_str());
            if (wp == sp && wr == sr && ws == ss) {
                printf("Case #%d: %s\n", tt, s.c_str());
                exist = true;
                break;
            }

        }
        if (!exist) {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        }



    }
}