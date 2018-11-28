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
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

const int N = 101;
const int K = 10*100+5;
int n, p, q;
int h[N], g[N];
int qc[N], pc[N];
int t[N][K];

void solve(int tc) {
    scanf("%d %d %d", &p, &q, &n);
    REP(i, n) scanf("%d %d", &h[i], &g[i]);
    REP(i, n) {
        qc[i] = (h[i]-1)/q+1;
        int r = h[i] - (qc[i]-1)*q;
        pc[i] = (r-1)/p+1;
    }

    REP(i, n+1) REP(j, K) t[i][j] = -1;
    t[0][1] = 0;
    FOR(i, 1, n) REP(j, K) {
        int jj;
        jj = j - qc[i-1];
        if (jj >= 0 && jj < K && t[i-1][jj] >= 0) {
            maxi(t[i][j], t[i-1][jj]);
        }
        jj = j - (qc[i-1]-1) + pc[i-1];
        if (jj >=0 && jj < K && t[i-1][jj] >= 0) {
            maxi(t[i][j], t[i-1][jj] + g[i-1]);
        }
    }

    int best = 0;
    REP(i,K) maxi(best, t[n][i]);

    printf("Case #%d: %d\n", tc, best);
}

int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int t; scanf("%d", &t);
    REP(i, t) solve(i+1);    

    return 0;
}

