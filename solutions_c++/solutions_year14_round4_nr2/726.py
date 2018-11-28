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

ifstream in("B-large.in");
//ifstream in("input.txt");
ofstream out("output.txt");

const int INF = 1000000000;

int inv(const vint &a, const vint &state, int i, int si)
{
    //cerr << __LINE__ << " " << i << " " << si << endl;
    int res = 0;
    int n = a.size();
    for (int j = 0; j < n; ++j) {
        if (j != i && state[j]) {
            if (si != state[j]) {
                res += ((j < i) ^ (state[j] < si));
            } else if (si == -1) {
                res += ((j < i) ^ (a[j] < a[i]));
            } else if (si == 1) {
                res += ((j < i) ^ (a[j] > a[i]));
            }
        }
    }
    //cerr << i << " " << si << " " << res << endl;
    return res;
}

void solve()
{
    int n;
    in >> n;
    vint a(n);
    vpint pairs;
    int i = 0;
    for (int &x : a) {
        in >> x;
        pairs.pb({-x, i});
        ++i;
    }
    sort(pairs.begin(), pairs.end());
    vint state(n);
    int inv_res = 0;
    for (const auto p : pairs) {
        int i = p.second;
        int miv = 1000000000;
        for (int si : {-1, 1}) {
            int invc = inv(a, state, i, si);
            if (invc < miv) {
                state[i] = si;
                miv = invc;
            }
        }
        inv_res += miv;
    }
    out << inv_res;
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
