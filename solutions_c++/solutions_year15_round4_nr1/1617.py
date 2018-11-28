#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Pegman

int main()
{
    int cases;
    cin >> cases;

    for (int caseno = 1; caseno <= cases; caseno++) {
        int R, C;
        cin >> R >> C;
        vector<string> grid(R);
        for (int i = 0; i < R; i++) {
            cin >> grid[i];
        }

        int ret = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grid[i][j] != '.') {
                    int up = 0;
                    int down = 0;
                    int left = 0;
                    int right = 0;
                    for (int y = 0; y < R; y++) {
                        if (grid[y][j] != '.' && y < i) {
                            up = 1;
                        }
                        if (grid[y][j] != '.' && y > i) {
                            down = 1;
                        }
                    }
                    for (int x = 0; x < C; x++) {
                        if (grid[i][x] != '.' && x < j) {
                            left = 1;
                        }
                        if (grid[i][x] != '.' && x > j) {
                            right = 1;
                        }
                    }
                    if (!up && !down && !left && !right) {
                        ret = -1;
                        break;
                    }
                    if ((up && grid[i][j] == '^') ||
                        (down && grid[i][j] == 'v') ||
                        (left && grid[i][j] == '<') ||
                        (right && grid[i][j] == '>')) {
                    } else {
                        ret += 1;
                    }
                }
            }
            if (ret < 0) {
                break;
            }
        }

        cout << "Case #" << caseno << ": ";
        if (ret >= 0) {
            cout << ret << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
