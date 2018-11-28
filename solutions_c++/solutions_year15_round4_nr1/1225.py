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
using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x))

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define FU(i, a, b) for(decltype(a) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)

#define FD(i, a, b) for (decltype(a) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)

#define mset(c, v) memset(c, v, sizeof(c))
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;
const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;


int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main() {
	int _42;
	scanf("%d", &_42);
	fu(_41, _42) {
		printf("Case #%d:", _41+1);
		int N, M;
		scanf("%d %d", &N, &M);
		vector<string> inp(N);
		for (auto &x : inp) {
			char buf[200];
			scanf(" %s", buf);
			x = buf;
		}
		int ans = 0;
		bool poss = true;
		fu(i, N) fu(j, M) if (inp[i][j] != '.') {
			int dx = 0, dy = 0;
			switch (inp[i][j]) {
				case '^': dx = -1; break;
				case '<': dy = -1; break;
				case 'v': dx = 1; break;
				case '>': dy = 1; break;
			}
			bool bad = false;
			FU(k, 1, 500) {
				int ii = i + k*dx, jj = j + k*dy;
				if (ii < 0 || ii >= N || jj < 0 || jj >= M) {
					bad = true;
					break;
				}
				if (inp[ii][jj] != '.') break;
			}
			if (!bad) continue;
			ans++;
			bool has = false;
			fu(ii, N) if (i != ii) if (inp[ii][j] != '.') has = true;
			fu(jj, M) if (j != jj) if (inp[i][jj] != '.') has = true;
			if (!has) poss = false;
		}
		if (!poss) printf(" IMPOSSIBLE\n");
		else printf(" %d\n", ans);
	}
	return 0;
}
