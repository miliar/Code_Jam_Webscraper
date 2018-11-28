#include <string>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cctype>
#include <queue>
#include <climits>
#include <sstream>
#include <cassert>
#include <iostream>
#include <cstdio>
#include <iostream>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR_EACH(it,v) for(__typeof((v).begin()) it = (v).begin(); it!=(v).end(); ++it)
#define show(x) cout << #x << ": " << x << endl;

template<typename T>
ostream& operator<<(ostream &o, const vector<T>&v){
    FOR_EACH(x, v){
        if(x==v.begin()) o << "[";
        else o << ", ";
        o << *x;
    }
    o << "]";
    return o;
}

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int>VI;
typedef vector<vector<int> >VII;

struct Event {
    LL p;
    LL x;
    explicit Event(LL p_, LL x_):p(p_),x(x_){
    }
    bool operator > (const Event & rh) const {
        if(x!=rh.x) return x>rh.x;
        return p<rh.p;
    }
};

const LL mod = 1000002013;
LL calc_cost(LL n, LL dist){
    return (n + n-dist+1)*dist/2 % mod;
}

priority_queue<Event, vector<Event>, greater<Event> >Q;
stack<Event>S;
void solve(){
    LL n,m;
    scanf("%lld %lld", &n, &m);
    LL res = 0;
    REP(i,m){
        LL o,e,p;
        scanf("%lld %lld %lld", &o, &e, &p);
        Q.push(Event(p,o));
        Q.push(Event(-p,e));
        res += calc_cost(n,e-o+1) * p;
        res %= mod;
    }
    while(!Q.empty()){
        Event e = Q.top(); Q.pop();
        //printf("event x %d, p %d\n", e.x, e.p);
        if(e.p > 0){
            S.push(e);
        } else {
            LL h = -e.p;
            while(h>0){
                Event s = S.top(); S.pop();
                LL mn = min(h, s.p);
                h-=mn;
                s.p-=mn;
                //printf("mn %d, start %d, stop %d\n", mn, s.x, e.x);

                res -= mn*calc_cost(n, e.x - s.x + 1);
                res %= mod;

                if(s.p){
                    S.push(s);
                }
            }
        }
    }
    res %= mod;
    if(res<0) res+=mod;
    printf("%lld\n", res);
}

int main(int argc,char *argv[]) {
    int T; scanf("%d", &T);
    for(int t=1; t<=T; t++){
        printf("Case #%d: ", t);
        solve();
    }
}
