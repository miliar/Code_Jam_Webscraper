#define y1 JulioCortasar
#define y2 GabrielGarciaMarquez
#include <cmath>
#undef y1
#undef y2

#include <ctime>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

#include <bitset>
#include <queue>
#include <deque>
#include <stack>
// #include <tuple>
#include <set>
#include <map>

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 42
#endif

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef double lf;

void initrand()
{
    ll seed;
    asm("rdtsc":"=A"(seed));
    srand(seed);
}

const int maxn = 1000;

int dp[maxn][maxn];
int n, data[maxn];

void solve()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> data[i];
    int ans = maxn * maxn * maxn;
    for (int msk = 0; msk < (1 << n); ++msk)
    {
        int cur = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
            {
                if (((msk >> i) & 1) && ((msk >> j) & 1) && data[i] < data[j])
                    ++cur;
                if (!((msk >> i) & 1) && !((msk >> j) & 1) && data[i] > data[j])
                    ++cur;
                if (((msk >> i) & 1) && !((msk >> j) & 1)) ++cur;
            }
        ans = min(ans, cur);
    }
    cout << ans << endl;
}

int main()
{
#ifdef LOCAL
// 	freopen("input.txt", "r", stdin);
#endif
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
#ifdef LOCAL
    cerr << "Time = " << clock() / 1000 << " ms." << endl;
#endif
	return 0;
}
