#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define FOR(i,b,e) for(int i=(b); i<(int)(e); i++)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define ALL(c) (c).begin(), (c).end()
#define mp make_pair
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll;

template<class T1,class T2> ostream& operator<<(ostream& o,const pair<T1,T2>& p){return o<<"("<<p.first<<","<<p.second<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T>& v){o<<"[";for(typename vector<T>::const_iterator i=v.begin();i!=v.end();++i){if (i != v.begin()) o << ", ";o<<(*i);}o<<"]";return o;}
template<class T> ostream& operator<<(ostream& o,const set<T>& s){o<<"{";for(typename set<T>::const_iterator i=s.begin();i!=s.end();++i){if(i!=s.begin())o<<", ";o<<(*i);}o<<"}";return o;}
template<class K,class V> ostream& operator<<(ostream& o,const map<K,V>& m){o<<"{";for(typename map<K,V>::const_iterator i=m.begin();i!=m.end();++i){if(i!=m.begin())o<<", ";o<<i->first<<":"<<i->second;}o<<"}";return o;}
template<class T> ostream& operator<<(ostream& o,const vector<vector<T> >& m){o<<"[\n";for(typename vector<vector<T> >::const_iterator i=m.begin();i!=m.end();++i){o<<"  "<<(*i);o<<(i+1!=m.end()?",\n":"\n");}o<<"]\n";return o;}
string bitstr(int n,int d=0){string r;for(int i=0;i<d||n>0;++i,n>>=1){r+=(n&1)?"1":"0";}reverse(r.begin(),r.end());return r;}

const ll MOD = 1000002013LL;

ll fare(ll u, ll v, ll N) {
    ll num = v - u;
    ll res = ((N + N - (num-1)) * num / 2) % MOD;
    return res;
}

ll optimizedCost(ll N, vector<ll>& o, vector<ll>& e, vector<ll>& p) {
    vector<pair<ll, ll> > vp;
    REP(i, o.size()) {
        vp.push_back(mp(o[i], -p[i]));
        vp.push_back(mp(e[i], p[i]));
    }
    sort(ALL(vp));
    priority_queue<pair<ll, ll> > que;

    ll res = 0;
    REP(i, vp.size()) {
        if (vp[i].second < 0) {
            que.push(mp(vp[i].first, -vp[i].second));
        } else {
            ll pos = vp[i].first;
            ll num = vp[i].second;
            while (num) {
                pair<ll, ll> tickets = que.top(); que.pop();
                ll use = min(tickets.second, num);
                res += fare(tickets.first, pos, N) * use;
                res %= MOD;
                num -= use;
                tickets.second -= use;
                if (tickets.second > 0) {
                    que.push(tickets);
                }
            }
        }
    }
    return res;
}

ll standardCost(ll N, vector<ll>& o, vector<ll>& e, vector<ll>& p) {
    ll res = 0;
    REP(i, o.size()) {
        res += fare(o[i], e[i], N) * p[i];
        res %= MOD;
    }
    return res;
}

ll solve(ll N, vector<ll>& o, vector<ll>& e, vector<ll>& p) {
    ll standard = standardCost(N, o, e, p);
    ll optimized = optimizedCost(N, o, e, p);
    return (standard - optimized + MOD) % MOD;
}

int main() {
    int T; cin >> T;
    REP(t, T) {
        int N, M; cin >> N >> M;
        vector<ll> o(M), e(M), p(M);
        REP(i, M) cin >> o[i] >> e[i] >> p[i];
        ll ans = solve(N, o, e, p);
        cout << "Case #" << (t+1) << ": " << ans << endl;
    }
}
