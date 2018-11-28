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
#define debug(x)  {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef complex<int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

typedef pair<PII, PII> edge;

PII next(PII dir) {
    if (dir.real() == 1) return PII(0,1);
    else if (dir.imag() == 1) return PII(-1, 0);
    else if (dir.real() == -1) return PII(0, -1);
    else return PII(1,0);
}

edge go(edge e, int i) {
    PII a = e.X;
    PII b = e.Y;
    PII d = next(b-a);
    if (i == 0) return MP(b+d, b);
    else return MP(a, a+d);
}
int r,c;
vector<string> T;

bool valid(PII v) {
    return 0 <= v.real() && v.real() <= r && 0 <= v.imag() && v.imag() <= c;
}

bool can_go(PII a, PII b) {
    if (!valid(a) || !valid(b)) return false;
    if (a.real() > b.real()) swap(a,b);
    if (a.imag() < b.imag()) {
        char &C = T[a.real()][a.imag()];
        if (C == '\\') return false;
        C = '/';
        return true;
    } else {
        char &C = T[a.real()][b.imag()];
        if (C == '/') return false;
        C = '\\';
        return true;
    }
}

bool can_go(edge e1, edge e2) {
    if (e1.X == e2.X) return can_go(e1.Y, e2.Y);
    else return can_go(e1.X, e2.X);
}

bool do_it(edge start, edge end) {
    while(start != end) {
        edge cur = go(start, 0);
        if (!can_go(start, cur)) cur = go(start, 1);
        if (!can_go(start, cur)) return false;
        start = cur;
    }
    return true;
}

PII pt(int i) {
    if (i < c) return PII(r, i);
    i -= c;
    if (i < r) return PII(r-i, c);
    i -= r;
    if (i < c) return PII(0, c-i);
    i -= c;
    return PII(i, 0);
}

edge start(int i) {
    return MP(pt(i), pt(i+1));
}

edge end(int i) {
    return MP(pt(i+1), pt(i));
}



void solve(int tc) {
    cout << "Case #" << tc << ":" << endl;
    cin >> r >> c;
    T = vector<string>(r, string(c, '.'));
    int n = (r+c);
    vector<int> C(2*n);
    REP(i, n) {
        int x,y;
        cin >> x >> y;
        --x;--y;
        C[x] = y;
        C[y] = x;
    }
    REP(_, n) {
        int prv = -1;
        bool ok = false;
        REP(i, 2*n) {
            if (C[i] == -1) continue;
            if (prv == C[i]) {
             //   debug(MP(C[i]+1, i+1));
                bool val = do_it(start(C[i]), end(i));
                if (!val) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
                C[C[i]] = -1;
                C[i] = -1;
                ok = true;
            //REP(j,r) cout << T[r-1-j] << endl;
                break;
            } else {
                prv = i;
            }
        }
        if (!ok) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    REP(i, r) REP(j,c) if (T[i][j] == '.') T[i][j] = '/';
    REP(i,r) cout << T[r-1-i] << endl;
}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    REP(i,t) solve(i+1);


    return 0;
}

