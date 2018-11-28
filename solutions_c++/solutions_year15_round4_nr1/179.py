#include <iostream>
#include <string>
#include <array>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;
int t, r, c;

int grid[105][105];
int directionX[5] = {0, 0, 1, 0, -1};
int directionY[5] = {0, -1, 0, 1, 0};

bool willFail(int ar, int ac, int dir) {
    if (dir == 0) {
        return false;
    }
    int dx = directionX[dir];
    int dy = directionY[dir];
    while (true) {
        ar += dy; ac += dx;
        if (ar < 0 || ac < 0 || ar >= r || ac >= c) {
            return true;
        }
        if (grid[ar][ac] != 0) {
            return false;
        }
    }
}

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                char tmp; int result;
                cin >> tmp;
                switch (tmp) {
                    case '.': result = 0; break;
                    case '^': result = 1; break;
                    case '>': result = 2; break;
                    case 'v': result = 3; break;
                    default: result = 4;
                }
                grid[i][j] = result;
                // cout << grid[i][j];
            }
            // cout << endl;

        }
        int changeCount = 0;
        bool failed = false;
        for (int i = 0; i < r; i++) {
            if (failed) break;
            for (int j = 0; j < c; j++) {
                if (willFail(i, j, grid[i][j])) {
                    for (int d = 1; d <= 4; d++) {
                        if (!willFail(i, j, d)) {
                            changeCount++;
                            break;
                        }
                        if (d == 4) {
                            failed = true;
                        }
                    }
                }
                if (failed) break;
            }
        }
        if (failed) {
            cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << test << ": " << changeCount << endl;

        }
    }
}
