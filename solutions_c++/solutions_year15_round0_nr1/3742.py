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

const int MAXN = 1010;
char buf[MAXN];
int n;

int solve() {
    int people = 0;
    int result = 0;
    for (int i = 0; i < n; i++) {
        while (people < i) {
            people++;
            result++;
        }
        people += buf[i] - '0';
    }
    return result;
}

int main() {
	int z; assert(scanf("%d", &z) == 1);
    for (int zz = 1; zz <= z; zz++) {
        assert(scanf("%d %s", &n, buf) == 2);
        n++;
        printf("Case #%d: %d\n", zz, solve());
	}
	return 0;
}
