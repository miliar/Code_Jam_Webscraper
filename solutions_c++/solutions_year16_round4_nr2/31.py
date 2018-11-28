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

LD doit(vector<LD> p) {
    //debugv(p);
    int n = SZ(p);
    assert(n % 2 == 0);
    vector<vector<LD>> D(n+1,vector<LD>(n+1, 0));
    D[0][0] = 1;
    REP(i, n) FOR(j, 0, i) {
        D[i+1][j] += D[i][j] * p[i];
        D[i+1][j+1] += D[i][j] * (1-p[i]);
    }
    //debug(D[n][n/2]);
    return D[n][n/2];
}

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    int n,k;
    cin >> n >> k;
    vector<LD> p(n);
    REP(i,n) cin >> p[i];
    sort(ALL(p));
    LD best = 0;
    FOR(a, 0, k) {
        vector<LD> q;
        REP(i, k-a) q.PB(p[i]);
        REP(i, a) q.PB(p[n-1-i]);
        maxi(best, doit(q));
    }
    cout << best << endl;


}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}

