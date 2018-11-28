#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstring>
#include<cstdio>
#include<iomanip>
#include<map>
#include<iostream>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>

#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define VAR(v,i) __typeof(i) v = (i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define debug(x) { cerr << #x <<" = " << (x) << endl; }
#define debugv(x) { cerr << #x << " = "; FORE(it, x) cerr << *it << ", "; cerr << endl;  }
#define dprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef pair<int, int> PII;;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;
template<class C> void mini(C&a4, C b4) { a4 = min(a4,b4); }
template<class C> void maxi(C&a4, C b4) { a4 = max(a4,b4); }
template<class T1, class T2> ostream& operator<<(ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", "<< pair.Y << ")"; };

const int M = 8;
const int N = 4;
int n, m;
string s[M];
int t[M];
set<string> ss[N];

int worst;
int worstC;

void choose(int k) {
    if (k < m) {
        REP(i, n) {
            t[k] = i;
            choose(k+1);
        }
        return;
    }

    REP(i, n) {
        ss[i].clear();
    }
    REP(i, m) {
        FOR(r, 0, (int)s[i].length()) {
            ss[t[i]].insert(s[i].substr(0, r));
        }
    }
    int res = 0;
    REP(i, n) res += ss[i].size();
    if (worst < res) { worst = res; worstC = 0; }
    if (worst == res) worstC++;
    return;
}

void solve(int tc) {
   
    cin >> m >> n; 
    REP(i, m) cin >> s[i];
    
    worst = 0;
    worstC = 0;

    choose(0);
    
    printf("Case #%d: %d %d\n", tc, worst, worstC);
}

int main() {
    ios_base::sync_with_stdio();
    int ttttc; cin >> ttttc;
    FOR(tttc, 1, ttttc) solve(tttc); 
    return 0;
}
