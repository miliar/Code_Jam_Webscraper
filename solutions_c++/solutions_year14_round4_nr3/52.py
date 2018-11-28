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
#define debug(x) //{ cerr << #x <<" = " << (x) << endl; }
#define debugv(x) //{ cerr << #x << " = "; FORE(it, x) cerr << *it << ", "; cerr << endl;  }
#define dprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef pair<int, int> PII;;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;
template<class C> void mini(C&a4, C b4) { a4 = min(a4,b4); }
template<class C> void maxi(C&a4, C b4) { a4 = max(a4,b4); }
template<class T1, class T2> ostream& operator<<(ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", "<< pair.Y << ")"; };

struct R {
    int l, r, u, d;
};

bool cross(const R& a, const R& b) {
    if (a.l > b.r) return false;
    if (b.l > a.r) return false;
    if (a.d > b.u) return false;
    if (b.d > a.u) return false;
    return true;
}

const int N = 1005;
int n, w, h;
R r[N];

bool done;
vector<int> lleft, rright;
void check() {
    REP(i, SZ(lleft)) {
        int ii = lleft[i];
        REP(j, SZ(rright)) {
            int jj = rright[j];
            if (cross(r[ii], r[jj])) {
                if (jj == n) done = true;
                lleft.PB(jj);
                rright[j] = rright.back();
                rright.pop_back();
                --j;   
            }
        }
    }
}

void grow() {
    for (int ii: lleft) {
        r[ii].l--;
        r[ii].r++;
        r[ii].u++;
        r[ii].d--;
    }
}

void solve(int tc) {
    scanf("%d %d %d", &w, &h, &n);
    REP(i, n) {
        scanf("%d %d %d %d", &r[i].l, &r[i].d, &r[i].r, &r[i].u);
        ++r[i].r;
        ++r[i].u;
    }
    r[n].u = h;
    r[n].d = 0;
    r[n].l = w;
    r[n].r = w+1;

    r[n+1].u = h;
    r[n+1].d = 0;
    r[n+1].l = -1;
    r[n+1].r = 0;

    lleft.clear();
    rright.clear();

    lleft.PB(n+1);
    REP(i, n+1) rright.PB(i);
    done = false;

    int c = 0;
    debugv(lleft);
    check();
    debugv(lleft);
    while (!done) {
        ++c;
        grow();
        check();
        debugv(lleft);
    }

    printf("Case #%d: %d\n", tc, c);
}

int main() {
    ios_base::sync_with_stdio();
   
    int ttttc; scanf("%d", &ttttc);
    FOR(tttc, 1, ttttc) solve(tttc); 
    return 0;
}
