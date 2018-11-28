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

struct Restr
{
    int x;
    int k;
    vint y;
    int ma;
    Restr(int x_, const vint &y_) : x(x_), k(y_.size()), y(y_), ma(max(x, *max_element(y.begin(), y.end()))) {}
    Restr(int x_, int y_) : x(x_), k(1), y{y_}, ma(max(x, y_)) {}
    void print() const
    {
        cerr << "x[" << x << "] > ";
        if (k == 1) {
            cerr << "x[" << y[0] << "]" << endl;
        } else {
            cerr << "min(";
            for (int i = 0; i < k; ++i) {
                if (i) {
                    cerr << ", ";
                }
                cerr << "x[" << y[i] << "]";
            }
            cerr << ")" << endl;
        }
    }
};

int n;
vint a, b;
vector<Restr> r;
vvint vr;
vint x;
vector<bool> used;

bool check(int tri)
{
    const Restr &tr = r[tri];
    int mi = n;
    for (int i : tr.y) {
        mi = min(mi, x[i]);
    }
    return x[tr.x] > mi;
}

bool checkall(int i)
{
    for (int tr : vr[i]) {
        if (!check(tr)) {
            return false;
        }
    }
    return true;
}

bool go(int i)
{
    if (i == n) {
        for (int q : x) {
            out << q + 1 << " ";
        }
        return true;
    }

    for (int j = 0; j < n; ++j) {
        if (used[j]) {
            continue;
        }
        x[i] = j;
        if (!checkall(i)) {
            continue;
        }
        used[j] = true;
        bool ok = go(i + 1);
        used[j] = false;
        if (ok) {
            return true;
        }
    }
    return false;
}

void solve()
{
    in >> n;
    a.resize(n), b.resize(n), vr.resize(n);
    for (int i = 0; i < n; ++i) {
        in >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        in >> b[i];
    }
    r.clear();
    for (int i = 1; i < n; ++i) {
        vint y;
        for (int j = 0; j < i; ++j) {
            if (a[i] <= a[j]) {     // x_j > x_i
                r.emplace_back(j, i);
            }
            if (a[j] + 1 == a[i]) {
                y.pb(j);
            }
        }
        if (!y.empty()) {
            r.emplace_back(i, y);
        }
    }
    for (int i = n - 2; i >= 0; --i) {
        vint y;
        for (int j = n - 1; j > i; --j) {
            if (b[i] <= b[j]) {     // x_j > x_i
                r.emplace_back(j, i);
            }
            if (b[j] + 1 == b[i]) {
                y.pb(j);
            }
        }
        if (!y.empty()) {
            r.emplace_back(i, y);
        }
    }
    int k = r.size();
    for (int i = 0; i < k; ++i) {
        const Restr &tr = r[i];
        //tr.print();
        vr[tr.ma].pb(i);
    }
    x.resize(n);
    used.assign(n, false);
    go(0);
    x.clear();
    r.clear();
    vr.clear();
    a.clear();
    b.clear();
    used.clear();
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
