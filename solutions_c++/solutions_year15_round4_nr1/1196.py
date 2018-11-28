#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <vector>
#include <string>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

//const char* inputFile = "file.in";
//const char* outputFile = "file.out";
//const char* inputFile = "A-small-attempt1.in";
//const char* outputFile = "A-small-attempt1.out";
const char* inputFile = "A-large.in";
const char* outputFile = "A-large.out";

const int INF = 1e9;

const char* dir = "^>v<";

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int getDir(char c) {
    for (int i = 0; i < 4; ++i) {
        if (dir[i] == c) {
            return i;
        }
    }
    return -1;
}

class Solver {
public:
    Solver() {
    }

    bool notValid(int i, int j) const {
        if (i < 0 || j < 0) {
            return true;
        }
        if (i >= R || j >= C) {
            return true;
        }
        return false;
    }

    int move(int i, int j, int dir, bool isFirst, bool haveMore = false) {
        //DB(i);
        //DB(j);
        if (!isFirst && visited[i][j]) {
            return 0;
        }

        if (!isFirst) {
            if (grid[i][j] != '.') {
                visited[i][j] = true;
                haveMore = true;
                dir = getDir(grid[i][j]);
            }
        }

        int ni = i + dx[dir];
        int nj = j + dy[dir];
       //DB(ni);
        //DB(nj);

        if (notValid(ni, nj)) {
            if (haveMore) {
                return 1;
            }
            return -1;
        }

        int cost = move(ni, nj, dir, false, haveMore);
        if (cost != -1) {
            return cost;
        } else {
            if (!haveMore) {
                return -1;
            } else {
                return 1;
            }
        }
    }

    string solveTest() {
        cin >> R >> C;
        grid.resize(R);
        for (int i = 0; i < R; ++i) {
            cin >> grid[i];
            //cout << grid[i] << endl;
        }

        int ans = 0;

        visited.assign(R, vector<char>(C, false));

        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (visited[i][j]) {
                    continue;
                }
                if (grid[i][j] == '.') {
                    continue;
                }
                visited[i][j] = true;

                int d = getDir(grid[i][j]);
                bool good = false;
                for (int k = 0; k < 4; ++k) {
                    int cost = move(i, j, (d + k) % 4, true, false);
                    if (cost != -1) {
                        // We managed to do this!
                        ans += cost + (k != 0);
                        good = true;
                        break;
                    }
                }
                if (!good) {
                    return "IMPOSSIBLE";
                }
            }
        }

        return std::to_string(ans);
    }
    vector<string> grid;
    vector<vector<char>> visited;
    int R, C, W;
};

int main() {
    freopen(inputFile, "r", stdin);
    freopen(outputFile, "w", stdout);
    int T;
    scanf("%d", &T);

    for (int testNumber = 1; testNumber <= T; ++testNumber) {
        Solver solver;
        string verdict = solver.solveTest();
        printf("Case #%d: %s\n", testNumber, verdict.c_str());
    }
    return 0;
}
