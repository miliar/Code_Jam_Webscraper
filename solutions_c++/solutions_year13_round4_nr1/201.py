#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)

#define forall(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

typedef long long tint;

tint MOD = 1000002013;
tint INV_2 = 500001007;

tint cost(tint d, tint N)
{
    return (((d * ((2*N+1-d) % MOD)) % MOD) * INV_2) % MOD;
}

int main()
{
    int TT; cin >> TT;
    forn(tt,TT)
    {
        set<tint> interesting;
        map<tint,tint> up,down;
        map<tint,tint> bag;
        tint N; cin >> N;
        int M; cin >> M;
        tint tCost = 0;
        forn(i,M)
        {
            tint o,e,p; cin >> o >> e >> p;
            interesting.insert(o);
            interesting.insert(e);
            up[o] += p;
            down[e] += p;
            tCost += (p * cost(e-o, N)) % MOD;
            tCost %= MOD;
        }
        tint res = 0;
        forall(it, interesting)
        {
            bag[*it] += up[*it];
            tint k = down[*it];
            while (k > 0)
            {
                while (bag.rbegin()->second == 0) bag.erase(--bag.end());
                tint bajan = min(k, bag.rbegin()->second);
                bag.rbegin()->second -= bajan;
                k -= bajan;
                res += (bajan * cost(*it - bag.rbegin()->first , N)) % MOD;
                res %= MOD;
            }
        }
        res = ((MOD + (tCost - res)) % MOD + MOD) % MOD;
        cout << "Case #" << tt+1 << ": " << res << endl;
        cerr << "Case #" << tt+1 << ": " << res << endl;
    }
    return 0;
}
