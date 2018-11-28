
#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

string B[13][3];



void solve(int tc) {
    cout << "Case #" << tc << ": ";
    int N;
    int R[3];
    cin >> N;
    assert(N <= 12);
    int tot = 1ll<<N;
    REP(i,3) cin >> R[i];
    bool ok = true;
    REP(i, 3) {
        if (abs(3*R[i] - tot) > 2) ok = false;
    }
    if (!ok) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    REP(i, 3) {
        if (abs(3*R[i] - tot) == 2) cout << B[N][i] << endl;
    }



}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    B[0][0] = "R";
    B[0][1] = "P";
    B[0][2] = "S";
    REP(i, 12) {
        REP(j, 3) {
            string x = B[i][(j+1)%3], y = B[i][(j+2)%3];
            if (x > y) swap(x,y);
            B[i+1][j] = x+y;
        }
    }

    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}

