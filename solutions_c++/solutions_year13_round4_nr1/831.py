#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair
#define MOD (1000002013LL)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll n, m;

struct Travel {
    ll from, to, num;
    Travel() {}
    Travel(ll from, ll to, ll num): from(from), to(to), num(num) {}
    bool operator < (const Travel &r) const {
        return (from != r.from ? from < r.from : (to != r.to ? to < r.to : num < r.num));
    }
};

vector<Travel> v;

void eraseEmpty(map<ll, ll> &M) {
    set<ll> toErase;
    for(map<ll, ll>::iterator it = M.begin(); it != M.end(); ++it) {
        if (it->second == 0) toErase.insert(it->first);
    }
    for(set<ll>::iterator it = toErase.begin(); it != toErase.end(); ++it) {
        M.erase(*it);
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i, j;
    int T, NT;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        v.clear();
        cin>>n>>m;
        for(i=0; i<m; ++i) {
            ll a, b, c;
            cin>>a>>b>>c;
            v.push_back(Travel(a, b, c));
        }
        v.push_back(Travel(n+1, n+1, 1));
        sort(v.begin(), v.end());
        ll exp = 0;
        for(i=0; i<m; ++i) {
            ll stops = v[i].to - v[i].from;
            ll cur = (stops*(stops-1)/2) % MOD;
            exp = (exp + v[i].num*cur) % MOD;
        }
//        map<pair<ll, ll>, ll> s;
//        map<pair<ll, ll>, ll>::iterator it;
        map<ll, ll> fromM, toM;
        map<ll, ll>::iterator it;
        ll res = 0;
        for(i=0; i<=m; ++i) {
            ll stop = v[i].from;
            ll toStop = v[i].to;
            ll people = v[i].num;
            for(it=toM.begin(); it != toM.end(); ++it) {
                if (it->first < stop) {
                    for(map<ll, ll>::reverse_iterator rit = fromM.rbegin(); rit != fromM.rend(); ++rit) {
                        if (rit->first > it->first) continue;
                        ll numPeople = min(rit->second, it->second);
                        if (numPeople > 0) {
                            rit->second -= numPeople;
                            it->second -= numPeople;
                            ll stops = it->first - rit->first;
                            ll cur = (stops * (stops-1) / 2) % MOD;
                            cur = (cur * numPeople) % MOD;
                            res = (res + cur) % MOD;
                        }
                    }
                }
            }
            eraseEmpty(fromM);
            eraseEmpty(toM);

            fromM[stop] += people;
            toM[toStop] += people;
//            for(it = s.begin(); it != s.end(); ++it) {
//                if ((*it).first.second < stop) {
//                    ll stops = ((*it).first.second)-((*it).first.first);
//                    ll cur = (stops*(stops-1)/2) % MOD;
//                    cur = (cur*((*it).second)) % MOD;
//                    res = (res + cur) % MOD;
//                    it->second = 0;
//                }
//            }
//            eraseEmpty(s);
//            for(it = s.begin(); it != s.end() && people>0; ++it) {
//                if (toStop > ((*it).first.second)) {
//                    ll numPeople = min(people, ((*it).second));
//                    if (numPeople > 0) {
//                        people -= numPeople;
//                        s[mp((*it).first.first, toStop)] += numPeople;
//                        (*it).second -= numPeople;
//                        s[mp(stop, (*it).first.second)] += numPeople;
//                    }
//                }
//            }
//            eraseEmpty(s);
//            if (people>0) {
//                s[mp(stop, toStop)] += people;
//            }
        }
        res = (res + MOD - exp) % MOD;
        cout<<"Case #"<<T<<": "<<res<<endl;
    }
    return 0;
}
