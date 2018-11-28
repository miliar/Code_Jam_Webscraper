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

ifstream in("D-small-attempt0.in");
ofstream out("output.txt");

bool av[4][4];
bool come[4];
bool busy[4];

bool go(int n, int i) {
    if (i == n) {
        return true;
    }
    for (int w = 0; w < n; ++w) {
        if (!come[w]) {
            come[w] = true;
            bool success = false;
            for (int j = 0; j < n; ++j) {
                if (!busy[j] && av[w][j]) {
                    success = true;
                    busy[j] = true;
                    if (!go(n, i + 1)) {
                        return false;
                    }
                    busy[j] = false;
                }
            }
            if (!success) {
                return false;
            }
            come[w] = false;
        }
    }
    return true;
}

void solve()
{
    int n;
    in >> n;
    int init0 = 0;
    bool *w[4 * 4];
    for (int i = 0; i < n; ++i) {
        string s;
        in >> s;
        for (int j = 0; j < n; ++j) {
            av[i][j] = (s[j] == '1');
            if (!av[i][j]) {
                w[init0++] = &av[i][j];
            }
        }
    }
    int ans = n * n;
    for (int mask = 0; mask < (1 << init0); ++mask) {
        int cost = 0;
        for (int i = 0; i < init0; ++i) {
            if (mask & (1 << i)) {
                *w[i] = true;
                ++cost;
            }
        }
        if (cost < ans) {
            memset(busy, 0, sizeof(bool) * n);
            memset(come, 0, sizeof(bool) * n);
            if (go(n, 0)) {
                ans = cost;
            }
        }
        for (int i = 0; i < init0; ++i) {
            if (mask & (1 << i)) {
                *w[i] = false;
            }
        }
    }
    out << ans;
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ": ";
        solve();
        out << endl;
    }

    return 0;
}
