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

char buf[110];
vector<string> in;
vi aloc;
vi ans;

int doit(vector<string>& T) {
	vector<string> prefix;
	for (auto &x : T) fu(i, SZ(x)+1) prefix.pb(x.substr(0, i));
	sort(all(prefix));
	return unique(all(prefix)) - prefix.begin();
}

void dfs(int i, int N) {
	if (i == SZ(in)) {
		int A = 0;
		fu(j, N) {
			vector<string> T;
			fu(k, SZ(in)) if (aloc[k] == j) T.pb(in[k]);
			A += doit(T);
		}
		ans.pb(A);
		return;
	}
	aloc.pb(0);
	fu(j, N) {
		aloc.back() = j;
		dfs(i+1, N);
	}
	aloc.pop_back();
}

int main() {
	int _42;
	scanf("%d", &_42);
	fu(_41, _42) {
		ans.clear();
		aloc.clear();
		in.clear();
		printf("Case #%d: ", _41+1);
		int M, N;
		scanf("%d %d", &M, &N);
		in.resize(M);
		for (auto &x : in) {
			scanf(" %s", buf);
			x = buf;
		}
		dfs(0, N);
		sort(all(ans));
		printf("%d ", ans.back());
		printf("%d\n", count(all(ans), ans.back()));
	}
	return 0;
}
