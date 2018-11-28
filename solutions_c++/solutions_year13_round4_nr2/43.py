#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }

Int solve1(Int N, Int P)
{
    --P;
    for (Int res = 0, resi = 1, pos = 0, i = N - 1; i >= 0; --i, ++resi) {
        pos += 1LL << i;
        if (P < pos) {
            return res;
        }
        res += 1LL << resi;
    }
    return (1LL << N) - 1;
}

Int solve2(Int N, Int P)
{
    --P;
    for (Int res = 0, resi = N - 1, pos = 0, i = 0; i < N; ++i, --resi) {
        pos += 1LL << i;
        if (P < pos) {
            return res;
        }
        res += 1LL << resi;
    }
    return (1LL << N) - 1;
}

int main()
{
    int T;
    cin >> T;

    for (int CN = 1; CN <= T; ++CN) {
        Int N, P;
        cin >> N >> P;

        cout << "Case #" << CN << ": " << solve1(N, P) << ' ' << solve2(N, P) << endl;
    }

    return 0;
}
