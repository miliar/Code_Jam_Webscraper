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

const int N = 1005;
LD naomi[N], ken[N];

void doit() {
    int n; scanf("%d", &n);
    REP(i, n) scanf("%Lf", &naomi[i]);
    REP(i, n) scanf("%Lf", &ken[i]);
    vector<LD> both;

    sort(naomi, naomi+n);
    sort(ken, ken+n);
/*
    printf("\n");
    REP(i, n) printf("%.2Lf ", naomi[i]);
    printf("\n");
    REP(i, n) printf("%.2Lf ", ken[i]);
    printf("\n");
*/
    int score = 0, p = 0, q = 0;
    REP(i, n) {
        while ((q < n) && (naomi[q] < ken[p])) {
            ++q;
        }
        if (q < n) {
            ++q;
            ++score;
        } else {
        }
        ++p;
    }

    printf("%d ", score);

    score = p = q = 0;
    REP(i, n) {
        while ((q < n) && (ken[q] < naomi[p])) {
            ++q;
        }
        if (q < n) {
            ++q;
        } else {
            ++score;
        }
        ++p;
    }

    printf("%d\n", score);
}

int main() {
    ios_base::sync_with_stdio();
    cout << fixed << setprecision(10);
    
    int tt; scanf("%d", &tt);
    REP(ttt, tt) {
        printf("Case #%d: ", ttt+1);
        doit();
    }

    return 0;
}
