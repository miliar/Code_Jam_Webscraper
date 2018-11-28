#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int main() {
    int dira[256], dirb[256];
    memset(dira, 0, sizeof(dira));
    memset(dirb, 0, sizeof(dirb));
    dira['^'] = -1;
    dirb['^'] = 0;
    dira['v'] = 1;
    dirb['v'] = 0;
    dira['>'] = 0;
    dirb['>'] = 1;
    dira['<'] = 0;
    dirb['<'] = -1;
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long R, C;
        cin >> R >> C;
        string g[R];
        for (int i = 0; i < R; i++) cin >> g[i];

        long count = 0;
        int impossible = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (g[i][j] == '.') continue;
                string s = " ^>v<";
                s[0] = g[i][j];
                int done = 0;
                for (int k = 0; k < s.size(); k++) {
                    if (done) break;
                    int a = dira[s[k]];
                    int b = dirb[s[k]];
                    int r = i + a;
                    int c = j + b;
                    while (r >= 0 && c >= 0 && r < R && c < C) {
                        //cout << r << " " << c << endl;
                        if (dira[g[r][c]] != 0 || dirb[g[r][c]] != 0) {
                            if (k) count += 1;
                            done = 1;
                            //cout << t << " " << k << endl;
                            break;
                        }
                        r += a;
                        c += b;
                    }
                }
                if (!done) {
                    impossible = 1;
                    break;
                }
            }
        }

        cout << "Case #" << t << ": ";
        cout << (impossible ? "IMPOSSIBLE" : to_string(count)) << endl;
    }
}
