#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
using namespace std;

const int MAXN = 120, MAXH = 120;
int board[MAXN][MAXN], n, m;

class Stat {
public:
    int count[MAXH];
    int diff_count, at_least, value, deleted;
    int row, col;

    void clear() {
        memset(count, 0, sizeof count);
        diff_count = 0;
        at_least = 0;
        value = -1;
        deleted = 0;
    }

    int decrease(int num) {
        at_least = num;
        if (--count[num] == 0) {
            --diff_count;
            for (int i = 0; i < MAXH; ++i) {
                if (count[i]) {
                    value = i;
                    break;
                }
            }
        }
        return 1;
    }

    void increase(int num) {
        if (count[num]++ == 0) {
            if (++diff_count == 1) {
                value = num;
            } else {
                value = -1;
            }
        }
    }

    bool operator<(const Stat &other) const {
        if (diff_count != other.diff_count) {
            return diff_count < other.diff_count;
        }
        return value < other.value;
    }
};

Stat row[MAXN], col[MAXN];

int main() {
    int tott;
    scanf("%d", &tott);
    for (int curt = 1; curt <= tott; ++curt) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf("%d", &board[i][j]);
            }
        }
        for (int i = 0; i < n; ++i) {
            row[i].clear();
            row[i].col = -1;
            row[i].row = i;
            for (int j = 0; j < m; ++j) {
                row[i].increase(board[i][j]);
            }
        }
        for (int j = 0; j < m; ++j) {
            col[j].clear();
            col[j].row = -1;
            col[j].col = j;
            for (int i = 0; i < n; ++i) {
                col[j].increase(board[i][j]);
            }
        }
        int row_remain = n, col_remain = m;
        while (row_remain && col_remain) {
            Stat *target = NULL;
            for (int i = 0; i < n; ++i) {
                if (!row[i].deleted && (!target || row[i] < *target)) {
                    target = &row[i];
                }
            }
            for (int j = 0; j < m; ++j) {
                if (!col[j].deleted && (!target || col[j] < *target)) {
                    target = &col[j];
                }
            }
            Stat cur = *target;
            if (cur.value == -1 || cur.value < cur.at_least) {
                break;
            }
            if (cur.col != -1) {
                for (int i = 0; i < n; ++i) {
                    row[i].decrease(cur.value);
                }
                --col_remain;
                col[cur.col].deleted = 1;
                //cerr << "DEL COL " << cur.col << endl;
            } else {
                for (int j = 0; j < m; ++j) {
                    col[j].decrease(cur.value);
                }
                --row_remain;
                row[cur.row].deleted = 1;
                //cerr << "DEL ROW " << cur.row << endl;
            }
        }
        printf("Case #%d: ", curt);
        if (row_remain && col_remain) {
            puts("NO");
        } else {
            puts("YES");
        }
    }
    return 0;
}
