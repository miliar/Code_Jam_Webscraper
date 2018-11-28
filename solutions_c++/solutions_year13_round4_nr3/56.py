
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
#define maxn 2005
int t[maxn][2];
int res[maxn];
bool done[maxn];
int n;

int dd[maxn][maxn][2];
int du[maxn][maxn][2];

int go(int kto) {
    if (kto > n) return 1;
    int x = 0;
    fup(j, 1, n) { dd[kto][j][0] = x; if (done[j]) maxi(x, t[j][0]); }
    x = INF;
    fup(j, 1, n) { du[kto][j][1] = x; if (!done[j]) mini(x, t[j][1]); }

    x = 0;
    fdo(j, n, 1) { dd[kto][j][1] = x; if (done[j]) maxi(x, t[j][1]); }

    x = INF;
    fdo(j, n, 1) { du[kto][j][0] = x; if (!done[j]) mini(x, t[j][0]); }
/*
    fup(i, 1, n) {
        cout << du[kto][i][0] << " " << du[kto][i][1] << endl;
    }*/

    fup(i, 1, n) if (!done[i]) {
        if (t[i][0] == dd[kto][i][0] + 1&& t[i][1] == dd[kto][i][1] + 1 && 
                (du[kto][i][0] > t[i][0]) && 
                (du[kto][i][1] > t[i][1])
                ) {
      //      cout << "TAK " << kto << " " << i << endl;
            done[i] = 1;
            res[i] = kto;
            if (go(kto + 1)) return 1;
            else {
                //cout << "KRUWA" << endl;
            }
            done[i] = 0;
        }

    }
    return 0;
}

void solve() {
    cin >> n;
    fup(j, 0, 1) fup(i, 1, n) cin >> t[i][j];
    CLR(done);
    go(1);
    fup(i, 1, n) cout << res[i] << " " ;
    cout << endl;
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

