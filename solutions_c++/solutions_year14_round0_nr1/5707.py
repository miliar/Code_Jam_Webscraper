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

int t[4][4];

void doit() {
    int poss[16];
    REP(i, 16) poss[i] = 0;

    REP(k, 2) {
        int l; scanf("%d", &l); --l;
        REP(i, 4) REP(j, 4) {
            scanf("%d", &t[i][j]);
            --t[i][j];
        }
        REP(j, 4) ++poss[t[l][j]];
    }

    int c = 0;
/*
    REP(i, 4) {
        REP(j, 4) {
            printf("%d ", t[i][j]);
        }
        printf("\n");
    }

    REP(i, 16) printf("%d ",poss[i]);
    printf("\n");
*/
    REP(i, 16) if (poss[i] == 2) ++c;
    if (c == 0) {
        printf("Volunteer cheated!\n");
    } else if (c > 1) {
        printf("Bad magician!\n");
    } else {
        REP(i, 16) if (poss[i] == 2) printf("%d\n", i+1);
    }
}

int main() {
    ios_base::sync_with_stdio();
    cout << fixed << setprecision(10);
    
    int tt;
    scanf("%d", &tt);
    REP(ttt, tt) {
        printf("Case #%d: ", ttt+1);
        doit();
    }
    
    return 0;
}
