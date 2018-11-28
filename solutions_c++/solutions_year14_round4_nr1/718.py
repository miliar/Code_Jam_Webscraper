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

void solve()
{
    int n, x;
    in >> n >> x;
    vint cnt(x + 1);
    for (int i = 0; i < n; ++i) {
        int cs;
        in >> cs;
        ++cnt[cs];
    }
    int res = 0;
    for (int size = x; size > 0; --size) {
        while (cnt[size]) {
            if (size * 2 <= x && cnt[size] >= 2) {
                ++res;
                cnt[size] -= 2;
            } else {
                int p = 0;
                for (int i = size - 1; i > 0; --i) {
                    if (cnt[i] && i + size <= x) {
                        p = i;
                        break;
                    }
                }
                if (p) {
                    ++res;
                    --cnt[size];
                    --cnt[p];
                } else {
                    ++res;
                    --cnt[size];
                }
            }
        }
    }
    out << res;
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
