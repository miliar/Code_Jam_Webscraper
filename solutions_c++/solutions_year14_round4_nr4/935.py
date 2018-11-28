#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <cmath>

using namespace std;

#define DBG(z) cerr << #z << ": " << (z) << endl
#define NEWL cerr << endl
#define passert(x, m) {if (!(x)) {cerr << m << "  ::  ";} assert(x);}
#define err(s) cerr << "[92m" << s << "[0m" << endl
#define LINE cerr << "DEBUG LINE: " << __LINE__ << endl

#define IT(v) __typeof((v).begin())
#define mem(f, a) memset(f, a, sizeof(f))
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define for_each(it, v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define next_int() ({int __t; scanf("%d", &__t); __t;})

const int MOD = 1000000007, INF = 100000000;

char tmp[501];
int M, N;
vector <string> str;
int ans[1 << 10], dp[1 << 10][10], dc[1 << 10][10];

int nodes(int msk) {
    int &ret = ans[msk];
    if (ret != -1) return ret;
    set <string> st;
    for (int i = 0; i < M; ++i) {
        if (msk & (1 << i)) {
            for (int j = 0; j <= str[i].size(); ++j)
                st.insert(str[i].substr(0, j));
        }
    }
    return ret = st.size();
}

int worst(int msk, int n) {
    if (n == 0) {
        if (msk == 0)
            return 0;
        else
            return -INF;
    }
    int &ret = dp[msk][n];
    if (ret != -1)
        return ret;
    ret = -INF;
    for (int sub = msk; sub > 0; sub = msk & (sub - 1)) {
        ret = max(ret, worst(sub, n - 1) + nodes(msk ^ sub));
    }
    ret = max(ret, worst(0, n - 1) + nodes(msk));
    return ret;
}

int count(int msk, int n) {
    if (n == 0) {
        if (msk == 0)
            return 1;
        else
            return 0;
    }
    int &ret = dc[msk][n];
    if (ret != -1) return ret;
    ret = 0;
    int r = worst(msk, n);
    for (int sub = msk; sub > 0; sub = msk & (sub - 1)) {
        if (r == worst(sub, n - 1) + nodes(msk ^ sub))
            ret = (ret + count(sub, n - 1)) % MOD;
    }
    if (r == worst(0, n - 1) + nodes(msk))
        ret = (ret + count(0, n - 1)) % MOD;
    return ret;
}

int main() {
    int T = next_int();
    for (int kase = 1; kase <= T; ++kase) {
        M = next_int(), N = next_int();
        mem(ans, -1), mem(dp, -1), mem(dc, -1);
        str.clear();
        for (int i = 0; i < M; ++i) {
            scanf("%s", tmp);
            str.push_back(tmp);
        }
        printf("Case #%d: %d %d\n", kase, worst((1 << M) - 1, N), count((1 << M) - 1, N));
    }
}

