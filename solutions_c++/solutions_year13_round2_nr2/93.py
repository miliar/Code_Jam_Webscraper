#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define SZ size()
#define PB push_back
#define SORT(a) sort((a).begin(), (a).end())
#define REV(a) reverse((a).begin(), (a).end())
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

ll N, X, Y;

long double C(ll n, ll k)
{
    long double res = 1.0;
    FOR(t, 0, k) res *= (long double)(n - t) / (long double)(t + 1);
    return res;

}

long double solve()
{
    if(X == 0 and Y == 0) return 1.0;
    if(X < 0) X *= -1;
    ll len = X + Y + 1;
    ll cnt = (len - 2) * (len - 1) / 2;
    //DEBUG(len);
    //DEBUG(cnt);
    if(cnt >= N) return 0.0;
    N -= cnt;
    //DEBUG(N);
    if(N >= len * 2 - 1) return 1.0;
    if(X == 0 and N == len * 2 - 1) return 1.0;
    if(X == 0 and N < len * 2 - 1) return 0.0;
    ll mx = Y + len - 1;
    if(N > mx) return 1.0;
    if(N <= Y) return 0.0;

    long double res = 1.0;
    for(ll h = 0; h <= Y; h++)
    {
        if(N - h > len - 1) continue;
        //cout << h << " " << N - h << endl;
        ll h1 = max(h, N - h), h2 = min(h, N - h);
        //cout << h1 << " " << h2 << endl;
        long double temp = 0.0;
        if(h1 == len - 1)
        {
            FOR(a, h1, N + 1)
            {
                if(a - 1 < 0 or h1 - 1 < 0 or a - 1 < h1 - 1) cout << "!!!!" << endl;
                long double temp2 = C(a - 1, h1 - 1);
                FOR(t, 0, a) temp2 *= 0.5;
                temp += temp2;
            }
        }
        else
        {
            temp = C(N, h2);
            //cout << "   " << temp << endl;
            FOR(t, 0, h1 + h2) temp *= 0.5;
        }
        //cout << temp << endl;
        res -= temp;
    }
    return res;
}

int main()
{
    freopen("Blarge.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> N >> X >> Y;
        cout << fixed << setprecision(20) << "Case #" << testNo << ": " << solve() << endl;
    }
}
