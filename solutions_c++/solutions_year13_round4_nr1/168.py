#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int64) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'
#ifdef CUTEBMAING
#include "cutedebug.h"
#else
#define debug(x) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint64;
typedef long double ld;

const int64 inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);

int64 n, m;
vector<int64> o, e, p;
vector<pair<int64, pair<int64, int64> > > ev;
map<int64, int64> started;

inline int64 f(int64 n, int64 dist){
    return n * (n + 1) / 2 - (n - dist) * (n - dist + 1) / 2;
}

const int64 M = 1000002013;

void run(){
    assert(scanf("%lld%lld", &n, &m));
    o.resize(m), e.resize(m), p.resize(m);
    for (int64 i = 0; i < m; i++){
        assert(scanf("%lld%lld%lld", &o[i], &e[i], &p[i]));
        if (o[i] > e[i])
            swap(o[i], e[i]);
    }
    ev.clear(), started.clear();
    for (int64 i = 0; i < m; i++)
        ev.pb(mp(o[i], mp(-1, i))), ev.pb(mp(e[i], mp(1, i)));
    sort(all(ev));
    int64 ans = 0;
    foreach(curEvent, ev){
        if (curEvent->sc.fs == -1)
            started[o[curEvent->sc.sc]] += p[curEvent->sc.sc];
        else{
            int64 k = p[curEvent->sc.sc];
            int64 curStation = curEvent->fs;
            while (k > 0){
                assert(len(started) > 0);
                map<int64, int64>::iterator it = started.end(); --it;
                int64 decrease = min(it->sc, k);
                int64 station = it->fs;
                ans = (ans + (f(n, curStation - station) % M) * decrease) % M;
                it->sc -= decrease, k -= decrease;
                if (it->sc == 0)
                    started.erase(it);
            }
        }
    }
    int64 realAns = 0;
    for (int64 i = 0; i < m; i++)
        realAns = (realAns + (f(n, e[i] - o[i]) % M) * p[i]) % M;
    printf("%lld\n", (realAns - ans + M) % M);
}

int main(){
    #if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
    #endif
    int t; assert(scanf("%d", &t));
    for (int i = 0; i < t; i++){
        printf("Case #%d: ", i + 1);
        run();
    }
    return 0;
}
