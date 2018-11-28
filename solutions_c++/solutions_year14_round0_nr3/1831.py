#include <iostream>
#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef pair<int, int> ii;
int r, c, m;
int rc;

const int moves[][2] = {
    {+1, +1}, {+1, +0}, {+1, -1},
    {+0, +1}, {+0, -1},
    {-1, +1}, {-1, +0}, {-1, -1}
};
const int moves_count = sizeof(moves) / sizeof(moves[0]);

vector<int> states[26];
void precompute_states()
{
    const int end_stt = 1<<25;
    for (int stt = 0; stt < end_stt; ++stt) {
        const int bombs = __builtin_popcount(stt);
        states[bombs].push_back(stt);
    }
}

namespace s1
{
    int stt;
    inline int index(const int row, const int col)
    {
        return row * c + col;
    }
    inline bool grid(const int row, const int col) // true: bomb, false: nothing
    {
        const int idx = index(row, col);
        return stt & (1<<idx);
    }
    bool has_adjacent_bomb[5][5];
    void precompute_adjacency()
    {
        memset(has_adjacent_bomb, 0, sizeof has_adjacent_bomb);
        for (int row = 0; row < r; ++row)
        for (int col = 0; col < c; ++col) {
            for (int i = 0; i < moves_count; ++i) {
                const int new_row = row + moves[i][0];
                const int new_col = col + moves[i][1];
                if (new_row >= 0 && new_row < r && new_col >= 0 && new_col < c && grid(new_row, new_col) == true) {
                    has_adjacent_bomb[row][col] = true;
                    break;
                }
            }
        }
    }

    bool visited[5][5];
    int visited_count = 0;
    void dfs(const int row, const int col)
    {
        if (row == -1 || row == r || col == -1 || col == c) return;
        if (visited[row][col]) return;
        visited[row][col] = true;
        ++visited_count;
        if (has_adjacent_bomb[row][col] == false) {
            dfs(row+1, col+1);
            dfs(row+1, col+0);
            dfs(row+1, col-1);
            dfs(row+0, col+1);
            dfs(row+0, col-1);
            dfs(row-1, col+1);
            dfs(row-1, col+0);
            dfs(row-1, col-1);
        }
    }
    int flood_fill(const int start_row, const int start_col)
    {
        memset(visited, 0, sizeof visited);
        visited_count = 0;
        dfs(start_row, start_col);
        return visited_count;
    }

    void solve()
    {
        const int nonbombs = rc - m;
        for (const int current_state : states[m]) {
            // ...
            stt = current_state;
            precompute_adjacency();
            // Find a starting position
            int start_row = -1, start_col = -1;
            for (int row = 0; row < r; ++row)
            for (int col = 0; col < c; ++col) {
                if (grid(row, col) == false && has_adjacent_bomb[row][col] == false) {
                    start_row = row;
                    start_col = col;
                    //break;
                    goto blabla;
                }
            }
blabla:
            if (start_row == -1) continue;
            // Test
            if (flood_fill(start_row, start_col) == nonbombs) {
                for (int row = 0; row < r; ++row) {
                    for (int col = 0; col < c; ++col)
                        if (start_row == row && start_col == col)
                            putchar('c');
                        else
                            putchar(grid(row, col) ? '*' : '.');
                    putchar('\n');
                }
                return;
            }
        }
        puts("Impossible");
    }
}

void run()
{
    scanf("%d%d%d", &r, &c, &m);
    rc = r*c;

    if (r == 1 && c == 1) {
        if (m == 0) {
            puts("c");
        } else {
            puts("Impossible");
        }
    } else if (m == rc-1) {
        for (int row = 0; row < r; ++row) {
            for (int col = 0; col < c; ++col)
                if (row == 0 && col == 0)
                    putchar('c');
                else
                    putchar('*');
            putchar('\n');
        }
    } else if (c == 1) {
        if (m <= r - 1) {
            putchar('c'), putchar('\n');
            int empty = r - m - 1;
            while (empty--)  putchar('.'), putchar('\n');
            int bombed = m;
            while (bombed--) putchar('*'), putchar('\n');
        } else {
            puts("Impossible");
        }
    } else if (r == 1) {
        if (m <= c - 1) {
            putchar('c');
            int empty = c - m - 1;
            while (empty--)  putchar('.');
            int bombed = m;
            while (bombed--) putchar('*');
            putchar('\n');
        } else {
            puts("Impossible");
        }
    } else { // c, r >= 2
        if (m == rc) {
            puts("Impossible");
        } else {
            /******************************************************** SOLVE ********************************************************/
            //printf("(b=%d)\n", m);
            s1::solve();
            /******************************************************** SOLVE ********************************************************/
        }
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2-try2.out", "w+", stdout);
    #endif
    precompute_states();

    int testcases;
    scanf("%d", &testcases);
    for (int test = 1; test <= testcases; ++test) {
        printf("Case #%d:\n", test);
        run();
    }

    return 0;
}
