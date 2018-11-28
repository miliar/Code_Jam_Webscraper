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

const ll MOD = 1000002013LL;

int N, M, O[1111], E[1111], P[1111];
ll in[2222], out[2222];

ll solve()
{
    ll a1 = 0, a2 = 0;

    FOR(i, 0, M)
    {
        ll d = O[i] - E[i];
        ll part = (((d * (d - 1) / 2) % MOD) * (ll)P[i]) % MOD;
        a1 = (a1 + part) % MOD;
    }

    set<int> S;
    FOR(i, 0, M)
    {
        S.insert(O[i]);
        S.insert(E[i]);
    }
    map<int, int> L, Linv;
    int cnt = 0;
    TR(it, S)
    {
        L[(*it)] = cnt;
        Linv[cnt] = (*it);
        cnt++;
    }
    memset(in, 0, sizeof(in));
    memset(out, 0, sizeof(out));
    FOR(i, 0, M)
    {
        in[L[O[i]]] += P[i];
        out[L[E[i]]] += P[i];
    }

    FOR(i, 0, cnt)
    {
        int ind = i;
        while(out[i])
        {
            if(in[ind])
            {
                ll t = min(in[ind], out[i]);
                in[ind] -= t;
                out[i] -= t;

                ll d = Linv[ind] - Linv[i];
                t %= MOD;
                ll part = (((d * (d - 1) / 2) % MOD) * t) % MOD;
                a2 = (a2 + part) % MOD;
            }
            ind--;
        }
    }

    return (a2 + MOD - a1) % MOD;
}

int main()
{
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> N >> M;
        FOR(i, 0, M) cin >> O[i] >> E[i] >> P[i];
        cout << "Case #" << testNo << ": " << solve() << endl;
    }
}



