#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int R, C;
string m[100];

int offset[4][2] = {
    {-1, 0},
    { 1, 0},
    {0,-1},
    {0, 1},
};

int solve() {
    int ans = 0;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (m[i][j] == '.') {
                continue;
            }
            int d;
            switch (m[i][j]) {
                case '^':
                    d = 0;
                    break;
                case 'v':
                    d = 1;
                    break;
                case '<':
                    d = 2;
                    break;
                case '>':
                    d = 3;
                    break;
            }

            bool possible = false;
            bool change = true;
            for (int k = 0; k < 4; k++) {
                int x = i;
                int y = j;
                while (true) {
                    x += offset[k][0];
                    y += offset[k][1];
                    if (x < 0 || x >= R || y < 0 || y >= C) {
                        break;
                    }
                    if (m[x][y] != '.') {
                        possible = true;
                        if (k == d) {
                            change = false;
                        }
                        break;
                    }
                }
            }

            if (!possible) {
                return -1;
            }
            if (change) {
                ans++;
            }
        }
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int ans = 0;
        cin >> R >> C;
        for (int i = 0; i < R; i++) {
            cin >> m[i];
        }
        ans = solve();

        cout << "Case #" << testcase << ": ";
        if (ans < 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}
