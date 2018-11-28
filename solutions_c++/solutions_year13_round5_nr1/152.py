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
#define MOD 1000002013

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int T, N;
ll B, X[37], bet[37];
bool undo[37];

ld win()
{
    ll prize = 0, loss = 0, nPrize = 0, mVal = 1ll<<42;
    for (int i = 0; i < 37; ++i)
    {
        mVal = min(mVal, X[i] + bet[i]);
        loss += bet[i];
    }
    for (int i = 0; i < 37; ++i)
    if (mVal == X[i] + bet[i])
    {
        prize += 36*bet[i];
        ++nPrize;
    }
    return ld(prize - nPrize*loss)/ld(nPrize);
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cout << setprecision(18);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> B >> N;
        memset(X, 0, sizeof X);
        for (int i = 0; i < N; ++i)
            cin >> X[i];
        sort(X, X + 37);
        ll lo = 0, hi = X[36]+1;
        while (lo < hi)
        {
            ll m = (lo + hi + 1) / 2, b = 0;
            for (int i = 0; i < 37; ++i)
                b += max(0ll, m - X[i]);
            if (b <= B)
                lo = m;
            else
                hi = m - 1;
        }
        for (int i = 0; i < 37; ++i)
            bet[i] = max(0ll, lo - X[i]), B -= bet[i];
        ld ans = win();
        memset(undo, false, sizeof undo);
        for (int i = 36; B; --i)
        {
            if (i < 0)
                cout << "ERROR" << endl;
            if (X[i] + bet[i] == lo)
                ++bet[i], --B, undo[i] = true;
            ans = max(ans, win());
        }
        for (int i = 0; i < 37; ++i)
            bet[i] -= undo[i];
        for (int k = 0; k < 4; ++k)
        for (int i = 0; i < 37; ++i)
        if (bet[i])
        {
            --bet[i];
            ans = max(ans, win());
        }
        cout << "Case #" << z << ": " << ans << endl;
    }
}
