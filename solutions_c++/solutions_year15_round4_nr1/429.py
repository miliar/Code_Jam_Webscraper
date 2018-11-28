#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 111;

int n, m;
char field[MAXN][MAXN];

int count(int x, int y, int dx, int dy) {
    int result = 0;
    while (true) {
        x += dx;
        y += dy;
        if (x < 0 || y < 0 || x >= n || y >= m) {
            break;
        }
        result += (field[x][y] != '.');
    }
    return result;
}

void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> field[i];
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (field[i][j] == '.' || answer == -1) {
                continue;
            }

            int up = count(i, j, -1, 0);
            int down = count(i, j, 1, 0);
            int left = count(i, j, 0, -1);
            int right = count(i, j, 0, 1);

            if (up + down + left + right == 0) {
                answer = -1;
            } else if (field[i][j] == '^' && up == 0) {
                answer += 1;
            } else if (field[i][j] == '>' && right == 0) {
                answer += 1;
            } else if (field[i][j] == 'v' && down == 0) {
                answer += 1;
            } else if (field[i][j] == '<' && left == 0) {
                answer += 1;
            }
        }
    }

    if (answer == -1) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << answer << "\n";
    }
}

int main() {
	int cases; cin >> cases;
	for (int i = 0; i < cases; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}