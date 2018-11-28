#include<cstdio>
#include<iostream>

using namespace std;

const int MAXN = 2000;
char s[MAXN];
int s_max;
int main() {
        int T;
        cin >> T;
        for (int cas = 1; cas <= T; ++cas) {
                cin >> s_max;
                cin >> s;
                int mx = 0;
                int ans = 0;
                for (int i = 0; i <= s_max; ++i) {
                        if (mx < i) {
                                ++ans;
                                ++mx;
                        }
                        mx += s[i] - '0';
                }
                cout << "Case #" << cas << ": " << ans << endl;
        }
        return 0;
}
