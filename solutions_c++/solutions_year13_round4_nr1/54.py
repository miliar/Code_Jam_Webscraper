
#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define fup FOR
#define fdo FORD
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define siz SZ
#define CLR(x) memset((x), 0, sizeof(x))
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int>P;
typedef vector<int>VI;
const int INF=1E9+7;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<typename T1, typename T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { out << "(" << pair.FI << ", " << pair.SE << ")"; return out; }

const LL mod = 1000002013;
LL n, m;

LL cost(LL l) {
    LL x = (l * (l - 1)) / 2;
    LL u = (l) * (LL)n;
    u -= x;
    u %= mod;
    u = (u + mod) % mod;
    return u;
}

bool comp(const pair<LL, LL> &l, const pair<LL, LL> &r) {
    if (l.FI != r.FI) return l.FI < r.FI;
    else return l.SE > r.SE;
}


void solve() {
    vector<pair<LL, LL> > events;
    cin >> n >> m;

    LL sum = 0;
    vector<pair<LL, LL> > stos;

    fup(i, 1, m) {
        LL s, e, p;
        cin >> s >> e >> p;
        events.PB(MP(s, p));
        events.PB(MP(e, -p));
        sum += (cost(e - s) * p) % mod;
        sum %= mod;
    }
    sum %= mod;

    sort(ALL(events), comp);
    LL sum2 = 0; 

    FORE(it, events) {
        LL x = it -> FI;
        LL il = it -> SE;
        //cout << "TTT " << x << " " << il << endl;
        if (il > 0) {
            stos.PB(MP(x, il));
        } else {
            il = -il;
            while (true) {
                LL il1 = stos.back().SE;
                //cout << "JOIN " << x << " " << stos.back().FI << endl;
                sum2 += cost(x - stos.back().FI) * min(il1, il);
                sum2 %= mod;
                stos.back().SE -= min(il1, il);
                il -= min(il1, il);
                if (il == 0) break;
                stos.pop_back();
            }
            if (il) stos.push_back(MP(x, il));
        }
    }
    sum %= mod;
    LL res = ((sum - sum2) % mod + mod) % mod;
    //cout << sum << " " << sum2 << endl;
    cout << res << endl;

}

int main(){
    ios_base::sync_with_stdio(false);

    int cas;
    cin >> cas;
    fup(c, 1, cas) {
        cout << "Case #" << c << ": ";
        solve();
    }



    return 0;
}

