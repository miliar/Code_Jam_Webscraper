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
#include<stack>
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
typedef pair<LL, LL>P;
typedef vector<int>VI;
const LL MOD=1000002013LL;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
#define MAXN 100007

LL N,M;

LL cost(LL len) {
    return ((len * (len - 1))/2) % MOD;
}

int main(){
	ios_base::sync_with_stdio(false);
    cout << setprecision(15) << fixed;
    int T;
    cin >> T;
    FOR(t,1,T) {
	    //in
        LL pocz = 0;
        map<LL, LL> MM;
        cin >> N >> M;
        while(M--){
            LL a,b,p;
            cin >> a >> b >> p;
            MM[a] += p;
            MM[b] -= p;
            pocz += p * cost(b-a);
            pocz %= MOD;
        }
	    //sol
        LL res = 0;
        stack<P> Q;
        FORE(i,MM) {
            if(i->Y > 0) {
                Q.push(P(*i));
            } else if(i->Y < 0) {
                LL x = -i->Y;
                while(x) {
                    assert(!Q.empty());
                    LL d = min(x, Q.top().Y);
                    res += (d%MOD) * cost(i->X - Q.top().X);
                    res %= MOD;
                    x -= d;
                    Q.top().Y -= d;
                    if(!Q.top().Y) Q.pop();
                }
            }
        }
        //cout << pocz << " -> " << res << endl;
        res = res - pocz;
        res %= MOD;
        if(res < 0) res += MOD;
	    //out
        cout << "Case #" << t << ": " << res << endl;
    }
	return 0;
}

