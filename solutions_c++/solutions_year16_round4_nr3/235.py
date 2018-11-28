#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <iomanip>

using namespace std;

#define pb push_back
#define f first
#define s second
typedef long long ll;
typedef pair<int, int> pint;
typedef pair<long long, long long> plint;
typedef vector<int> vint;
typedef vector<vector<int>> vvint;
typedef vector<long long> vlint;
typedef vector<vector<long long>> vvlint;
typedef vector<pair<int, int>> vpint;
typedef vector<pair<long long, long long>> vplint;

ifstream in("C-small-attempt0.in");
ofstream out("output.txt");

int r, c;
bool uptop[16][16];

struct Dir {
    int di, dj;

    bool operator == (const Dir &ot) const {
        return di == ot.di && dj == ot.dj;
    }
};

Dir dirs[4] = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

struct Cell {
    int i, j;

    Cell(int i, int j) : i(i), j(j) {}

    explicit Cell(int idx) {
        if (idx <= c) {
            i = 0;
            j = 2 * (idx - 1) + 1;
        } else if (idx <= c + r) {
            j = 2 * c;
            i = 2 * (idx - c - 1) + 1;
        } else if (idx <= c + r + c) {
            i = 2 * r;
            j = 2 * (c - (idx - c - r)) + 1;
        } else {
            j = 0;
            i = 2 * (r - (idx - 2 * c - r)) + 1;
        }
    }

    bool operator<(const Cell &other) const {
        return i < other.i || (i == other.i && j < other.j);
    }

    bool operator==(const Cell &other) const {
        return i == other.i && j == other.j;
    }

    Cell operator+(const Dir &dir) const {
        return {i + dir.di, j + dir.dj};
    }

    bool in_bounds() const {
        return i >= 0 && i <= 2 * r && j >= 0 && j <= 2 * c;
    }

    bool allow(const Dir &dir) const {
        Cell next = *this + dir;
        if (!next.in_bounds()) {
            return false;
        }
        if (i % 2 == 0) {
            if (dir == Dir{-1, -1}) {
                return !uptop[i / 2 - 1][j / 2];
            } else if (dir == Dir{-1, 1}) {
                return uptop[i / 2 - 1][j / 2];
            } else if (dir == Dir{1, -1}) {
                return uptop[i / 2][j / 2];
            } else {
                return !uptop[i / 2][j / 2];
            }
        } else {
            if (dir == Dir{-1, -1}) {
                return !uptop[i / 2][j / 2 - 1];
            } else if (dir == Dir{-1, 1}) {
                return uptop[i / 2][j / 2];
            } else if (dir == Dir{1, -1}) {
                return uptop[i / 2][j / 2 - 1];
            } else {
                return !uptop[i / 2][j / 2];
            }
        }
    }
};

bool go(const Cell &source, const Cell &target, set<Cell> &visited) {
    visited.insert(source);
    if (source == target) {
        return true;
    }
    for (const Dir &dir : dirs) {
        Cell next = source + dir;
        if (source.allow(dir) && !visited.count(next) && go(next, target, visited)) {
            return true;
        }
    }
    return false;
}

void solve()
{
    in >> r >> c;
    int np = 2 * (r + c);
    int px, x;
    vpint lovers;
    lovers.reserve(np / 2);
    for (int i = 0; i < np; ++i) {
        in >> x;
        if (i % 2 == 1) {
            lovers.emplace_back(px, x);
        }
        px = x;
    }
    out << endl;
    int cells = r * c;
    for (int mask = 0; mask < (1 << cells); ++mask) {
        int mc = mask;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                uptop[i][j] = mc & 1;
                mc >>= 1;
            }
        }

        bool ok = true;
        set<Cell> visited;
        for (const auto &lv : lovers) {
            Cell source(lv.f);
            Cell target(lv.s);
            if (!go(source, target, visited)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    out << (uptop[i][j] ? '/' : '\\');
                }
                if (i < r - 1) {
                    out << endl;
                }
            }
            return;
        }
    }
    out << "IMPOSSIBLE";
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ":";
        solve();
        out << endl;
    }

    return 0;
}
