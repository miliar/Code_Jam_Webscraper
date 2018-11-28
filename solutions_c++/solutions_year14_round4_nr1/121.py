#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iostream>
#include <utility>
#include <cctype>
using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x))

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)

#define mset(c, v) memset(c, v, sizeof(c))
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define SZ(c) int((c).size())

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;
const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;


int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main() {
	int _42;
	scanf("%d", &_42);
	fu(_41, _42) {
		printf("Case #%d: ", _41+1);
		int N, L;
		scanf("%d %d", &N, &L);
		vi t(N);
		for (int& x : t) scanf("%d", &x);
		sort(all(t));
		vi ja(N, 0);
		int ans = 0;
		int last = N-1;
		fu(i, N) if (!ja[i]) {
			ja[i] = 1;
			ans++;
			for (;last >= 0; --last) {
				if (ja[last]) continue;
				if (t[i] + t[last] > L) continue;
				ja[last] = 1;
				break;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
