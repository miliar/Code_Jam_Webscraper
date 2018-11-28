#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <functional>
#include <cstdint>
#include <cmath>
#include <unordered_set>
#include <unordered_map>
#include <sstream>

#define D(x) x

using namespace std;

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        int R, C;
        cin >> R >> C;

        vector<string> grid(R);
        for (int i = 0; i < R; i++) {
            cin >> grid[i];
        }

        const int UP = 1, LEFT = 2, DOWN = 4, RIGHT = 8;

        vector<vector<int>> dirs(R, vector<int>(C));

        for (int i = 0; i < R; i++) {
            bool arrow = false;
            for (int j = 0; j < C; j++) {
                if (arrow) dirs[i][j] |= LEFT;
                char c = grid[i][j];
                if (c == '<' || c == '>' || c == '^' || c == 'v') arrow = true;
            }
        }
        for (int i = 0; i < R; i++) {
            bool arrow = false;
            for (int j = C-1; j >= 0; j--) {
                if (arrow) dirs[i][j] |= RIGHT;
                char c = grid[i][j];
                if (c == '<' || c == '>' || c == '^' || c == 'v') arrow = true;
            }
        }
        for (int j = 0; j < C; j++) {
            bool arrow = false;
            for (int i = 0; i < R; i++) {
                if (arrow) dirs[i][j] |= UP;
                char c = grid[i][j];
                if (c == '<' || c == '>' || c == '^' || c == 'v') arrow = true;
            }
        }
        for (int j = 0; j < C; j++) {
            bool arrow = false;
            for (int i = R-1; i >= 0; i--) {
                if (arrow) dirs[i][j] |= DOWN;
                char c = grid[i][j];
                if (c == '<' || c == '>' || c == '^' || c == 'v') arrow = true;
            }
        }

        bool impossible = false;
        int changes = 0;
        for (int i = 0; i < R; i++) {
            if (impossible) break;
            for (int j = 0; j < C; j++) {
                char c = grid[i][j];
                if (c == '<' || c == '>' || c == '^' || c == 'v') {
                    if (dirs[i][j] == 0) {
                        impossible = true;
                        break;
                    }
                    if (c == '<' && !(dirs[i][j] & LEFT)) changes++;
                    if (c == '>' && !(dirs[i][j] & RIGHT)) changes++;
                    if (c == '^' && !(dirs[i][j] & UP)) changes++;
                    if (c == 'v' && !(dirs[i][j] & DOWN)) changes++;
                }
            }
        }

        cout << "Case #" << testCase << ": ";
        if (impossible) {
            cout << "IMPOSSIBLE";
        } else {
            cout << changes;
        }
        cout << endl;
    }
}
