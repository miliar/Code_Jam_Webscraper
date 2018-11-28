#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
 #include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
 #include <complex>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
 #define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
 #define MP make_pair
#define F first
#define S second
#define Aint(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()
#define PII pair<int, int>

#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define LL long long
#define mod 1000002013

using namespace std;

struct tInfor{
    int pos, enter, num;
};

vector<tInfor> infor;
multiset <PII > S;
int n, m;

tInfor MI(int pos, int enter, int num) {
    tInfor a;
    a.pos = pos;
    a.enter = enter;
    a.num = num;

    return a;
}

bool cmp(tInfor a, tInfor b) {
    if (a.pos != b.pos) return a.pos < b.pos;
    if (a.enter != b.enter) return a.enter > b.enter;
    return a.num > b.num;
}

long long call(int u, int v) {
    long long res = 0;
    long long K = v - u;
    long long N = n;
    res = (2LL * N - K) * (K + 1) / 2 % mod;

    return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("aBig.out", "w", stdout);
    int nTest;
    cin >> nTest;

    FOR (test, 1, nTest) {
        cout << "Case #" << test << ": ";
        cin >> n >> m;

        infor.clear();
        long long res = 0;

        FOR (i, 1, m) {
            int u, v, p;
            cin >> u >> v >> p;

            infor.PB(MI(u, 1, p));
            infor.PB(MI(v, -1, p));
            res = (res + call(u, v) * p) % mod;
        }

        sort(infor.begin(), infor.end(), cmp);
        //FOREACH(it, infor) cout << it->pos << " " << it->enter << " " << it->num << endl;

        FOREACH(it, infor)
        if (it->enter == 1)
            S.insert(MP(-(it->pos), it->num));
        else {
            int cnt = it->num;
            while (cnt) {
                set<PII >:: iterator pos = S.begin();
                PII p = *pos;
                S.erase(pos);

                int tmp = min(cnt, p.second);
                res = (res - call(-(p.first), it->pos) * tmp % mod) % mod;
                //cerr << -(p.first) << " " << it->pos << " " << tmp << endl;
                p.second -= tmp;
                cnt -= tmp;
                if (p.second) S.insert(p);
            }
        }

        res = (res + mod) % mod;
        cout << res << endl;
    }
    return 0;
}



