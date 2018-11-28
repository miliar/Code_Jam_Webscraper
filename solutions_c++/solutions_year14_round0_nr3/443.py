#include <iostream>
#include <vector>
#include <iomanip>
#include <set>

using namespace std;

int T, R, C, M, F;
std::vector<std::vector<char>> resultBoard;
bool impossible;


void printBoard(bool transpose) {
    if (impossible) {
        cout << "Impossible\n";
    }
    else {
        if (transpose) {
            for (int row = 0; row < C; ++row) {
                for (int col = 0; col < R; ++col) {
                    cout << resultBoard[col][row];
                }
                cout << "\n";
            }
        }
        else {
            for (int row = 0; row < R; ++row) {
                for (int col = 0; col < C; ++col) {
                    cout << resultBoard[row][col];
                }
                cout << "\n";
            }
        }
    }
}

void fillRectangle(int w, int h) {
    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            if (r == 0 && c == 0)
                continue;
            if (r < h && c < w)
                resultBoard[r][c] = '.';
            else
                resultBoard[r][c] = '*';
        }
    }
}

bool tryRectangles() {
    int size, rest;
    for (int height = 2; height <= R; ++height) {
        for (int width = 2; width <= C; ++width) {
            size = height * width;
            rest = F - size;
            if (size > F || rest == 1) {
                continue;
            }
            if (rest == 0) {
                fillRectangle(width, height);
                return true;
            }
            if (rest < height && width < C) {
                fillRectangle(width, height);
                for (int row = 0; row < rest; ++row) {
                    resultBoard[row][width] = '.';
                }
                return true;
            }
            if (rest < width && height < R) {
                fillRectangle(width, height);
                for (int col = 0; col < rest; ++col) {
                    resultBoard[height][col] = '.';
                }
                return true;
            }
        }
    }
    return false;
}


std::vector<int> cols;

bool partition(int sum, int colNum, int prev) {
    if (colNum == 1) {
        if (sum == prev) {
            cols[0] = sum;
            return true;
        }
        else {
            return false;
        }
    }

    for (int i = prev; i >= sum / colNum; --i) {
        if (prev == R && i == R-1) {
            continue;
        }
        if (sum >= i && partition(sum - i, colNum-1, i)) {
            cols[colNum-1] = i;
            return true;
        }
    }

    return false;
}

void printPartition() {
    for (int row = 0; row < R; ++row) {
        for (int col = 0; col < C; ++col) {
            if (row == 0 && col == 0)
                continue;

            if (row < R - cols[col])
                resultBoard[row][col] = '.';
            else
                resultBoard[row][col] = '*';
        }
    }
}

bool brut() {
    cols = std::vector<int>(C, 0);

    if (partition(M, C, R)) {
        printPartition();
        return false;
    }
    else {
        return true;
    }
}

void solve(bool transpose) {
    if (transpose) {
        swap(C,R);
    }
    F = R * C - M;
    impossible = true;
    resultBoard = std::vector<std::vector<char>>(R, std::vector<char>(C));
    resultBoard[0][0] = 'c';

    if (R == 1) {
        impossible = false;
        for (int i = 1; i <= F-1; ++i) {
            resultBoard[0][i] = '.';
        }
        for (int i = F; i < C; ++i) {
            resultBoard[0][i] = '*';
        }
    }
    else if (F == 1) {
        impossible = false;
        fillRectangle(1, 1);
    }
    else {
        if (tryRectangles()) {
            impossible = false;
        }
        else {
            impossible = brut();
        }
    }

    printBoard(transpose);
}

int main() {
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ":\n";
        cin >> R >> C >> M;
        solve(C < R);
    }
/*    for (int r = 1; r <= 50; ++r) {
        for (int c = 1; c <= 50; ++c) {
            R = r; C = c;
            for (int i = 0; i < r*c; ++i) {
                M = i;
                cout << "Case #" << r << " " << c << " " << i << ":\n";
                solve(C < R);
            }
        }
    }*/
}

