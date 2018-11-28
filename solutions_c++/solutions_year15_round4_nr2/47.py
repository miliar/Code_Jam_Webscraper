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

int T, N;
ll V, X;
pll src[100];

void reaf(ll& r)
{
    ld f;
    cin >> f;
    r = ll(f*10000 + 0.5);
}

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> N;
        reaf(V), reaf(X);
        ld rate = 0;
        ll dtemp = 0;
        bool hot = false, cold = false;
        for (int i = 0; i < N; ++i)
        {
            reaf(src[i].second), reaf(src[i].first);
            src[i].first -= X;
            rate += src[i].second;
            dtemp += src[i].first * src[i].second;
            hot |= src[i].first >= 0;
            cold |= src[i].first <= 0;
        }
        cout << "Case #" << z << ": ";
        if (hot && cold)
        {
            if (dtemp > 0)
            {
                dtemp *= -1;
                for (int i = 0; i < N; ++i)
                    src[i].first *= -1;
            }
            sort(src, src + N);
            for (int i = 0; i < N && dtemp < 0; ++i)
            {
                rate -= min(ld(src[i].second), ld(dtemp)/ld(src[i].first));
                dtemp -= src[i].first * src[i].second;
            }
            ld ans = ld(V) / rate;
            cout << fixed << setprecision(15) << ans << endl;
        }
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
