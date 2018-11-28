#define debug if(1)
// Grzegorz Guspiel
#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<int(n);++i)
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FORD(i,a,b) for (int i=((int)(a))-1; i>=(b); --i)
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define SIZE(c) ((int)((c).size()))
#define ALL(v) (v).begin(), (v).end()
#define VAR(v) #v << " " << v << " "
#define pb push_back
#define mp make_pair
#define st first
#define nd second

template<typename T> void maxE(T& a, const T& b) { a = max(a, b); }
template<typename T> void minE(T& a, const T& b) { a = min(a, b); }

template<typename T>
ostream& operator<<(ostream& out, const vector<T>& t_) {
    out << "[";
    for (auto i : t_) out << i << ", ";
    out << "]";
    return out;
}

template<typename S, typename T>
ostream& operator<<(ostream& out, const pair<S, T>& rhs) {
    out << "(" << rhs.st << "," << rhs.nd << ")";
    return out;
}

const int INF = 1000 * 1000 * 1000 + 100;

multiset<int> s;

int solve() {
    int best = INF;
    for (int mv = 1; mv <= *--s.end(); mv++) {
        int r = mv;
        for (auto i : s) r += (i + mv - 1) / mv - 1;
        minE(best, r);
    }
    return best;
}

int main() {
    ios_base::sync_with_stdio(0);
	int z; assert(scanf("%d", &z) == 1);
    for (int zz = 1; zz <= z; zz++) {
        int n; assert(scanf("%d", &n) == 1);
        s.clear();
        REP (i, n) {
            int tmp; assert(scanf("%d", &tmp) == 1);
            s.insert(tmp);
        }
        printf("Case #%d: %d\n", zz, solve());
	}
	return 0;
}
