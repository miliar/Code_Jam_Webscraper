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
#define MAXN 100007
#define LIM ((LL)(1E7))

bool pal(LL x) {
    stringstream ss;
    ss << x;
    string s;
    ss >> s;
    int n = SZ(s);
    REP(i,n)
        if(s[i] != s[n-1-i])
            return false;
    return true;
}

vector<LL> v;

int main(){
	ios_base::sync_with_stdio(false);
    cout << setprecision(15) << fixed;
    REP(i,LIM+1) {
        if(i%100000 == 0) debug(i);
        if(pal(i) && pal(((LL)i)*i))
            v.PB(((LL)i)*i);
    }
    v.PB(LIM*LIM+1);
    int T;
    cin >> T;
    FOR(t,1,T) {
	    //in
        LL A,B;
        cin >> A >> B;
	    //sol        
        int a = lower_bound(ALL(v), A) - v.begin();
        int b = lower_bound(ALL(v), B) - v.begin();
        if(v[b] > B) b--;
	    //out
        cout << "Case #" << t << ": " << (b-a+1) << endl;
    }
	return 0;
}
