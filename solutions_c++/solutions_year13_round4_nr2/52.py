
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

int n;
LL al;

LL worst(LL a) {
    LL x = (1LL << (n - 1));
    LL s = 0;
    while (a) {
        a = (a - 1) / 2;
        s += x;
        x /= 2;
    }
    return s + 1;
}

LL bes(LL a) {
    a = al - a - 1;
    LL s = 0;
    LL g = al;
    while (a) {
        g /= 2;
        a = (a - 1) / 2;
    }
    return g;
}

void solve() {
    LL P;
    cin >> n >> P;
    al = (1LL << n);
    
    LL s, e, best = -1;
    //debug(bes(6));

    s = 0; e = al - 1;
    while (s <= e) {
        LL q = (s + e) / 2;
        LL w = worst(q);
        if (w <= P) {
            best = q;
            s = q + 1;
        } else e = q - 1;
    }

    LL best2 = -1;
    s = 0; e = al - 1;

    while (s <= e) {
        LL q = (s + e) / 2;
        LL b = bes(q);
        if (b <= P) {
            best2 = q;
            s = q + 1;
        } else e = q - 1;
    }
    cout << best << " " << best2 << endl;
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

