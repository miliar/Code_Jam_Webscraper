#include <string>
#include <cstring>
#include <cassert>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

#define MOD 1000000007

int N, S;

int next[1000005][26];
int ilu[1000005];
int rozstaw_na[1005][1005];
int noverk[1005][1005];
int wolny;

pii analizuj(int x) {
    if (ilu[x]<=S) {
        int wyn = ilu[x];
        REP(a, 26)
            if (next[x][a]>=0)
                wyn += analizuj(next[x][a]).first;
        return MP(wyn, rozstaw_na[S][ilu[x]]);
    }
    bool jest_duzy = 0;
    int silu = 0;
    REP(a, 26) {
        if (next[x][a]>=0)
            silu += ilu[next[x][a]];
        if (next[x][a]>=0 && ilu[next[x][a]]>=S)
            jest_duzy = 1;
    }
    if (jest_duzy) {
        int suma = S;
        int spos = 1;
        REP(a, 26)
            if (next[x][a]>=0) {
                pii w2 = analizuj(next[x][a]);
                suma += w2.first;
                if (ilu[next[x][a]]>=S)
                    spos = spos*(LL)w2.second%MOD;
                else
                    spos = spos*(LL)rozstaw_na[S][ilu[next[x][a]]]%MOD;
            }
        if (ilu[x]>silu) // slowo w x
            spos = spos*(LL)S%MOD; 
        return MP(suma, spos);
    }
    else {
        int suma = S;
        int dziel[105];
        REP(a, S+1)
            dziel[a] = 1;
        REP(a, 26)
            if (next[x][a]>=0) {
                pii w2 = analizuj(next[x][a]);
                suma += w2.first;
                REP(dz, S+1)
                    if (dz<ilu[next[x][a]])
                        dziel[dz] = 0;
                    else
                        dziel[dz] = dziel[dz]*(LL)rozstaw_na[dz][ilu[next[x][a]]]%MOD;
            }
        if (ilu[x]>silu) { // slowo w x
                REP(dz, S+1)
                    if (dz<1)
                        dziel[dz] = 0;
                    else
                        dziel[dz] = dziel[dz]*(LL)rozstaw_na[dz][1]%MOD;
        }
        int spos = 0;
        REP(a, S+1) {
            int dzdz = dziel[a]*(LL)noverk[S][a]%MOD;
            if ((S-a)%2) 
                spos = (spos+MOD-dzdz)%MOD;
            else
                spos = (spos+dzdz)%MOD;
        }
        return MP(suma, spos);
    }
}

void init(int x) {
    REP(a, 26)
        next[x][a] = -1;
    ilu[x] = 0;
}

int daj_syna(int x, int lit) {
    if (next[x][lit]<0) {
        init(wolny);
        next[x][lit] = wolny++;
    }
    assert(wolny<1000005);
    return next[x][lit];
}

int main() {
    int TT;
    scanf("%d", &TT);
    FOR(y, 0, 100) {
            rozstaw_na[y][0] = 1;
            FOR(x, 1, y)
                rozstaw_na[y][x] = (rozstaw_na[y][x-1]*(LL)(y-x+1))%MOD;
    }
    noverk[0][0] = 1;
    FOR(n, 1, 100)
        FOR(k, 0, n)
            noverk[n][k] = ((k ? noverk[n-1][k-1] : 0)+(k<n ? noverk[n-1][k] : 0))%MOD;
    REP(tt, TT) {
        scanf("%d%d", &N, &S);
        
        init(0);
        wolny = 1;
        REP(a, N) {
            char buf[1000];
            scanf("%s", buf);
            int x = 0;
            char *p = buf;
            ++ilu[x];
            while (*p) {
                x = daj_syna(x, *p-'A');
                ++ilu[x];
                ++p;
            }
        }
        pii wyn = analizuj(0);
        printf("Case #%d: %d %d\n", (tt+1), wyn.first, wyn.second);
    }
}


