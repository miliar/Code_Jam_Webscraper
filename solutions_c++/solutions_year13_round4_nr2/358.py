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

ll N, P, firstLose, lastWin, a1, a2;

bool canLose(ll x)
{
    if(P == (1LL << N)) return 0;
    ll better = x;
    ll size = 1;
    FOR(i, 0, N)
    {
        if(!((firstLose >> i) & 1))
        {
            if(size > better) return 0;
            else better -= size;
        }
        else
        {
            if(size <= better) return 1;
        }
        size *= 2;
    }
    return 1;
}

bool canWin(ll x)
{
    ll worse = (1LL << N) - 1 - x;
    ll size = 1;
    FOR(i, 0, N)
    {
        if((lastWin >> i) & 1)
        {
            if(size > worse) return 0;
            else worse -= size;
        }
        else
        {
            if(size <= worse) return 1;
        }
        size *= 2;
    }
    return 1;
}

ll solve()
{
    firstLose = lastWin = 0;
    FOR(i, 0, N) firstLose |= ((ll)(!((P >> i) & 1)) << (N - 1 - i));
    FOR(i, 0, N) lastWin |= ((ll)(!(((P - 1) >> i) & 1)) << (N - 1 - i));

    ll l, r, m;

    if(P == (1LL << N)) a1 = (1LL << N) - 1;
    else
    {
        l = 0;
        r = (1LL << N) - 1;
        while(l + 1 < r)
        {
            m = (l + r) / 2;
            if(canLose(m)) r = m;
            else l = m;
        }
        while(canLose(r - 1)) r--;
        a1 = r - 1;
    }

    {
        l = 0;
        r = (1LL << N) - 1;
        while(l + 1 < r)
        {
            m = (l + r) / 2;
            if(canWin(m)) l = m;
            else r = m;
        }
        while(l < r and canWin(l + 1)) l++;
        a2 = l;
    }
}

int main()
{
    freopen("Blarge.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> N >> P;
        solve();
        cout << "Case #" << testNo << ": " << a1 << " " << a2 << endl;
    }
}



