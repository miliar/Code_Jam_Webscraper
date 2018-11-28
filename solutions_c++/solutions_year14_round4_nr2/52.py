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

const int N = 1000;
int n;
int a[N];

void solve(int tc) {
    scanf("%d", &n);
    REP(i, n) scanf("%d", &a[i]);
    vector<PII> que;
    REP(i, n) que.PB(MP(a[i], i));
    sort(ALL(que));

    int sum = 0;
    REP(i, n) {
        int p = que[i].Y;
        int l = 0, r = 0;
        REP(i, p) if (a[i] > a[p]) ++l;
        FOR(i, p+1, n-1) if (a[i] > a[p]) ++r;
        sum += min(l,r);
    }
    printf("Case #%d: %d\n", tc, sum);
}

int main() {
    ios_base::sync_with_stdio();   
    int ttttc; scanf("%d", &ttttc);
    FOR(tttc, 1, ttttc) solve(tttc); 
    return 0;
}
