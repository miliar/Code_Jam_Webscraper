#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int f[4][4] = {{0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
int g[4][4] = {{1, 1, 1, 1}, {1, -1, 1, -1}, {1, -1, -1, 1}, {1, 1, -1, -1}};

int main() {

	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

    int T, ca = 0;
    cin >> T;
    while (T--) {
        int L, X;
        cin >> L >> X;
        string str, s;
        cin >> str;
        for (int i = 0; i < X; ++i) {
            s += str;
        }
        for (int i = 0; i < L * X; ++i) {
            if (s[i] == 'i') s[i] = '1';
            if (s[i] == 'j') s[i] = '2';
            if (s[i] == 'k') s[i] = '3';
        }

        int sign = 1, val = 0;
        bool i_ansed = false, j_ansed = false, k_ansed = false;
        for (int i = 0; i < L * X; ++i) {
            int new_val = s[i] - '0';
            int new_sign = g[val][new_val];
            val = f[val][new_val];
            sign *= new_sign;
            if (!i_ansed && sign == 1 && val == 1) {
                sign = 1;
                val = 0;
                i_ansed = true;
                continue;
            }
            if (i_ansed && !j_ansed && sign == 1 && val == 2) {
                sign = 1;
                val = 0;
                j_ansed = true;
            }
        }
        string ans = "NO";
        if (i_ansed && j_ansed && sign == 1 && val == 3) ans = "YES";
        printf("Case #%d: ", ++ca);
        puts(ans.c_str());
    }
    return 0;
}
