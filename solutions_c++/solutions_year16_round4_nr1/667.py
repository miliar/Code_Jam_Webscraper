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

ifstream in("A-large.in");
ofstream out("output.txt");

struct Counter {
    int p, r, s;

    Counter operator+(const Counter &other) const {
        return {p + other.p, r + other.r, s + other.s};
    }

    bool operator==(const Counter &other) const {
        return p == other.p && r == other.r && s == other.s;
    }
};

using Row = vector<Counter>;

void print(int n, int p)
{
    if (n == 0) {
        out << string("PRS")[p];
    } else if (p == 0) {
        print(n - 1, 0);
        print(n - 1, 1);
    } else if (p == 1) {
        print(n - 1, 0);
        print(n - 1, 2);
    } else if (p == 2) {
        print(n - 1, 1);
        print(n - 1, 2);
    }
}

void solve()
{
    Counter cnt;
    int n;
    in >> n >> cnt.r >> cnt.p >> cnt.s;

    vector<Row> rows(n + 1, vector<Counter>(3));
    rows[0] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    for (int i = 1; i <= n; ++i) {
        Row &row = rows[i];
        const Row &prow = rows[i - 1];
        row[0] = prow[0] + prow[1];
        row[1] = prow[0] + prow[2];
        row[2] = prow[1] + prow[2];
    }
    const Row &row = rows.back();
    if (row[0] == cnt) {
        print(n, 0);
    } else if (row[1] == cnt) {
        print(n, 1);
    } else if (row[2] == cnt) {
        print(n, 2);
    } else {
        out << "IMPOSSIBLE";
    }
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
