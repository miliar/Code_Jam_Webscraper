#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int T, N, K, s[1000], v[1000], lo[100], hi[100];

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        memset(s, 0, sizeof s);
        memset(v, 0, sizeof v);
        memset(lo, 0, sizeof lo);
        memset(hi, 0, sizeof hi);
        cin >> N >> K;
        for (int i = K-1; i < N; ++i)
            cin >> s[i];
        int ans = 0;
        for (int i = K; i < N; ++i)
        {
            v[i] = v[i-K] + s[i]-s[i-1];
            lo[i%K] = min(lo[i%K], v[i]);
            hi[i%K] = max(hi[i%K], v[i]);
            ans = max(ans, hi[i%K]-lo[i%K]);
        }
        int mn = 0, mx = 0, sumK = (5000*K+s[K-1]) % K;
        for (int i = 0; i < K; ++i)
        {
            mn += ans-lo[i];
            mx += 2*ans-hi[i];
        }
        while (mn < mx && mn%K != sumK)
            ++mn;
        if (mn%K != sumK)
            ++ans;
        cout << "Case #" << z << ": " << ans << endl;
    }
}
