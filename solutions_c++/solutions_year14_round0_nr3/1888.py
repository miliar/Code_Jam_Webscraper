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

ifstream in("C-small-attempt2.in");
//ifstream in("input.txt");
ofstream out("output.txt");

int r, c, m;
vector<vector<bool>> mine;
vector<vector<bool>> zero;

void print(int fi, int fj)
{
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            char sym = (i == fi && j == fj ? 'c' : '.');
            if (mine[i][j]) {
                sym = '*';
            }
            out << sym;
        }
        out << endl;
    }
}

void dfs(vector<vector<bool>> &used, int &zero_cnt, int i, int j)
{
    --zero_cnt;
    used[i][j] = true;

    for (int ii = i - 1; ii <= i + 1; ++ii) {
        for (int jj = j - 1; jj <= j + 1; ++jj) {
            if (ii >= 0 && ii < r && jj >= 0 && jj < c && !used[ii][jj] && zero[ii][jj]) {
                dfs(used, zero_cnt, ii, jj);
            }
        }
    }
}

bool check()
{
    int zi = -1, zj = -1, fi = -1, fj = -1, zero_cnt = 0;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            int anc = 0;
            for (int ii = i - 1; ii <= i + 1; ++ii) {
                for (int jj = j - 1; jj <= j + 1; ++jj) {
                    if (ii >= 0 && ii < r && jj >= 0 && jj < c) {
                        anc += mine[ii][jj];
                    }
                }
            }
            zero[i][j] = (anc == 0);
            if (zero[i][j]) {
                zi = i, zj = j;
            }
            zero_cnt += zero[i][j];
            if (!mine[i][j]) {
                fi = i, fj = j;
            }
        }
    }

    if (m == r * c - 1) {
        print(fi, fj);
        return true;
    }
    if (zi == -1) {
        return false;
    }

    vector<vector<bool>> used(r, vector<bool>(c, false));
    dfs(used, zero_cnt, zi, zj);
    if (zero_cnt > 0) {
        return false;
    }

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (!mine[i][j] && !zero[i][j]) {
                bool has_anc = false;
                for (int ii = i - 1; ii <= i + 1; ++ii) {
                    for (int jj = j - 1; jj <= j + 1; ++jj) {
                        if (ii >= 0 && ii < r && jj >= 0 && jj < c && zero[ii][jj]) {
                            has_anc = true;
                        }
                    }
                }
                if (!has_anc) {
                    return false;
                }
            }
        }
    }
    print(zi, zj);

    return true;
}

int next_i(int i, int j)
{
    return (j == c - 1 ? i + 1 : i);
}

int next_j(int j)
{
    return (j + 1) % c;
}

bool go(int i, int j, int mine_rest, int rest)
{
    /*cerr << mine_rest << endl;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cerr << mine[i][j];
        }
        cerr << endl;
    }*/
    if (mine_rest > rest) {
        return false;
    }

    if (mine_rest == 0) {
        return check();
    }

    for (bool mine_cur : {false, true}) {
        mine[i][j] = mine_cur;
        //cerr << "set " << mine_cur << " at (" << i << ", " << j << ")" << endl;
        if (go(next_i(i, j), next_j(j), mine_rest - mine[i][j], rest - 1)) {
            return true;
        }
    }
    mine[i][j] = false;

    return false;
}

void solve()
{
    out << endl;

    in >> r >> c >> m;
    mine.clear();
    zero.clear();
    mine.resize(r, vector<bool>(c, false));
    zero.resize(r, vector<bool>(c, false));
    if (!go(0, 0, m, r * c)) {
        out << "Impossible" << endl;
    }
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ":";
        solve();
        //out << endl;
    }

    return 0;
}
