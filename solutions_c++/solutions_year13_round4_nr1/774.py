/*
TASK:  
LANG: C++
USER: smilitude
DATE: 2013-06-01 Sat 11:16 PM    
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<cassert>
#include<climits>
using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--) 
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()

#define sz size()
#define pb push_back

long long n;
map<int,long long> ticket, drop;
long long ans;
long long mod = 1000002013;

long long sum(long long d) {
    return (d*(d+1)/2) % mod;
}

long long score(long long d) {
    if( d == 0 ) return 0;
    long long ret = ( n * d ) % mod;
    ret -= sum(d-1);
    ret %= mod;
    if( ret < 0 ) ret += mod;
    return ret;
}

void unload( long long pos, long long population )  {
    vector< pair<int, long long> > v;
    // dumping
    FORIT(i,ticket) v.pb( *i );
    FORD(i,v.sz-1,0) {
        if( v[i].first > pos ) continue;
        long long cantake = min( v[i].second, population );
        v[i].second -= cantake;
        population -= cantake;
        ans -= ( cantake * score(pos-v[i].first) ) % mod;
        ans %= mod;
        if( ans < 0 ) ans += mod;
    }
    // update
    REP(i,v.sz) ticket[ v[i].first ] = v[i].second;
}

int main() {
        
    int t, m, ncase = 0;
    cin >> t;

    while( t-- ) {
        cin >> n >> m;
        ticket.clear();
        drop.clear();
        
        ans = 0;
        
        REP(_,m) {
            long long a, b, p;
            cin >> a >> b >> p;
            ticket[a] += p;
            drop[b] += p;
            ans += p * score( b-a );
            ans %= mod;
        }
        
        FORIT(i,drop) unload( i->first, i->second );
        printf("Case #%d: %lld\n", ++ncase, ans );
    }

    return 0;
}

