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

void solve()
{
    int n;
    string s;
    in >> s;
    n = s.length();
    int M = 1 << n;
    vector<double> f(M, 0);
    for (int m = 1; m < M; ++m) {
        int p = -1;
        for (int i = 0; i < n; ++i) {
            if (m & (1 << i)) {
                p = i;
                break;
            }
        }
        for (int i = n - 1; i >= 0; --i) {
            if (m & (1 << i)) {
                p = i;
            }
            f[m] += n - (p - i + n) % n + f[m - (1 << p)];
        }
        f[m] /= n;
        //out << m << " " << f[m] << endl;
    }
    int mask = 0;
    for (int i = 0; i < n; ++i) {
        mask += (s[i] == '.') * (1 << i);
    }
    out.precision(20);
    out << f[mask];
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
