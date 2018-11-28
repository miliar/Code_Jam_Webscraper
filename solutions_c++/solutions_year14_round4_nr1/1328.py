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

const int maxn = 10000;

int n, x;
multiset<int> data;

void solve()
{
    cin >> n >> x;
    for (int i = 0; i < n; ++i)
    {
        int tmp;
        cin >> tmp;
        data.insert(tmp);
    }
    int ans = 0;
    while (data.size())
    {
        auto last = --data.end();
        data.erase(last);
        auto y = data.upper_bound(x - *last);
        if (y != data.begin())
        {
            --y;
            data.erase(y);
        }
        ++ans;
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
