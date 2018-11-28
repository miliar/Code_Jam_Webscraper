
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
typedef pair<int, int> P;
typedef vector<int> VI;
const int INF=1E9+7;
template<class C> void mini(C&a4, C b4) { a4 = min(a4, b4); }
template<class C> void maxi(C&a4, C b4) { a4 = max(a4, b4); }

void solve(int tcas) {
    cout << "Case #" << tcas << ":";
    VI t;
    int n;
    cin >> n;
    fup(i, 1, n) { int a; cin >> a; t.PB(a); }
    int sum = 0;
    fup(i, 1, n) {
        int idx = 0;
        fup(j, 0, siz(t) - 1) if (t[j] < t[idx]) idx = j;
        int c1 = idx;
        int c2 = siz(t) - 1 - idx;
        sum += min(c1, c2);
        t.erase(t.begin() + idx);
    }

    cout << " " << sum << endl;
}

int main(){
    ios_base::sync_with_stdio(false);
    int cas;
    cin >> cas;
    fup(c, 1, cas) {
        solve(c);
    }
    return 0;
}

