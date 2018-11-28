#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstdint>
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

ifstream in("input.txt");
ofstream out("output.txt");

int64_t convert(int64_t x, int base)
{
    int64_t res = 0;
    int64_t pow = 1;
    while (x) {
        char d = x & 1;
        res += pow * d;
        pow *= base;
        x >>= 1;
    }
    return res;
}

int32_t find_divisor(int64_t x)
{
    for (int i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
            return i;
        }
    }
    return -1;
}

bool is_jamcoin(int64_t x, vector<int64_t> &divs)
{
    divs.resize(9);
    for (int base = 2; base <= 10; ++base) {
        auto y = convert(x, base);
        auto d = find_divisor(y);
        if (d == -1) {
            //cerr << convert(x, 10) << " failed at base " << base << ": " << y << " is prime" << endl;
            return false;
        } else {
            divs[base - 2] = d;
        }
    }
    return true;
}

void solve()
{
    int n, j;
    in >> n >> j;
    int64_t last = 1ll << n;
    int cnt = 0;
    vector<int64_t> divs;
    for (int64_t x = (1ll << (n - 1)) + 1; x < last && cnt < j; x += 2) {
        //cerr << "try " << x << endl;
        if (is_jamcoin(x, divs)) {
            out << convert(x, 10);
            for (int64_t d : divs) {
                out << " " << d;
            }
            out << endl;
            divs.clear();
            cerr << (++cnt) << endl;
        }
    }
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ":" << endl;
        solve();
        //out << endl;
    }

    return 0;
}
