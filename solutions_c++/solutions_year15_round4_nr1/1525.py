#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <utility>
#include <numeric>
#include <string.h>

using namespace std;

typedef unsigned long long ulong;
typedef unsigned int uint;
typedef long long int64;


inline ulong max(ulong a, ulong b) {
    return a > b ? a : b;
}

inline ulong min(ulong a, ulong b) {
    return a < b ? a : b;
}

enum Dir {
    EMPTY = -1,
    UP,
    RIGHT,
    DOWN,
    LEFT,
    NUM_DIRS,
};

//int DX[] = [-1, 0, 1, 0];
//int DY[] = [0, 1, 0, -1];

Dir grid[200][200];
int cnt[200][200];

inline Dir charToDir(char c) {
    switch(c) {
        default:
        case '.':
            return EMPTY;
        case '^':
            return UP;
        case '>':
            return RIGHT;
        case 'v':
            return DOWN;
        case '<':
            return LEFT;
    }

}

inline Dir nextDir(Dir d) {
    return (Dir)((d + 1) % NUM_DIRS);
}

bool processUp(int r, int c) {
    bool res = true;
    for (int j = 0; j < c; ++j) {
        int i = 0;
        for(; i < r; ++i) {
            if (grid[i][j] != EMPTY) {
                if (grid[i][j] == UP) {
                    cnt[i][j] = 1;
                    //cerr << "change " << i << ' ' << j << " from ^ to >\n";
                    grid[i][j] = RIGHT;
                    res = false;
                }
                break;
            }
        }
    }
    return res;
}

bool processRight(int r, int c) {
    bool res = true;
    for (int i = 0; i < r; ++i) {
        int j = c - 1;
        for(; j >= 0; --j) {
            if (grid[i][j] != EMPTY) {
                if (grid[i][j] == RIGHT) {
                    cnt[i][j] = 1;
                    //cerr << "change " << i << ' ' << j << " from > to v\n";
                    grid[i][j] = DOWN;
                    res = false;
                }
                break;
            }
        }
    }
    return res;
}

bool processDown(int r, int c) {
    bool res = true;
    for (int j = 0; j < c; ++j) {
        int i = r - 1;
        for(; i >= 0; --i) {
            if (grid[i][j] != EMPTY) {
                if (grid[i][j] == DOWN) {
                    cnt[i][j] = 1;
                    //cerr << "change " << i << ' ' << j << " from v to <\n";
                    grid[i][j] = LEFT;
                    res = false;
                }
                break;
            }
        }
    }
    return res;
}

bool processLeft(int r, int c) {
    bool res = true;
    for (int i = 0; i < r; ++i) {
        int j = 0;
        for(; j < c; ++j) {
            if (grid[i][j] != EMPTY) {
                if (grid[i][j] == LEFT) {
                    cnt[i][j] = 1;
                    //cerr << "change " << i << ' ' << j << " from < to ^\n";
                    grid[i][j] = UP;
                    res = false;
                }
                break;
            }
        }
    }
    return res;
}

int main() {
    //cerr << nextDir(UP) <<  ' ' << nextDir(LEFT) << endl;
    ulong numTests = 0;
    cin >> numTests;
    for (ulong t = 1; t <= numTests; ++t) {
        int r,c;
        cin >> r >> c;

        memset(grid, 0, sizeof(grid));
        memset(cnt, 0, sizeof(cnt));
        string line; 

        for (int i = 0; i < r; ++i) {
            cin >> line;
            if (line.length() != c) {
                cerr << "ERROR!!!\n";
            }

            for (int j = 0; j < line.length(); ++j) {
                grid[i][j] = charToDir(line[j]);
                ////cerr << grid[i][j] << ' ';
            }
            ////cerr << endl;
            ////cerr << "***************\n";
        }

        //cerr << "processUp\n";
        processUp(r, c);
        //cerr << "processRight\n";
        processRight(r, c);
        //cerr << "processDown\n";
        processDown(r, c);
        //cerr << "processLeft\n";
        processLeft(r, c);
        //cerr << "processUp\n";
        processUp(r, c);
        //cerr << "processRight\n";
        processRight(r, c);
        //cerr << "processDown\n";
        processDown(r, c);
        //cerr << "processLeft\n";
        processLeft(r, c);
        //cerr << "processUp\n";
        processUp(r, c);
        //cerr << "processRight\n";
        processRight(r, c);
        //cerr << "processDown\n";
        processDown(r, c);
        //cerr << "processLeft\n";
        processLeft(r, c);

        //cerr << "check up\n";
        if (!processUp(r, c)) {
            cout << "Case #" << t << ": IMPOSSIBLE"  << endl;
            continue;
        }

        int sum = 0;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                sum += cnt[i][j];

        cout << "Case #" << t << ": "  << sum << endl;
    }
    return 0;
}

