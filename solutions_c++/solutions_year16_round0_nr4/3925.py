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

int T, K, C, S;

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> K >> C >> S;
        cout << "Case #" << z << ":";
        if (S*C < K)
        {
            cout << " IMPOSSIBLE" << endl;
            continue;
        }
        int digit = 0;
        for (int i = 0; i < S && digit < K; ++i)
        {
            ll tile = 1, base = 1;
            for (int j = 0; j < C && digit < K; ++j)
            {
                tile += digit * base;
                base *= K; ++digit;
            }
            cout << ' ' << tile;
        }
        cout << endl;
    }
}
