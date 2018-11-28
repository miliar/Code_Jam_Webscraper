#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."
#define pi pair < int, int >

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAX_N = (int)1e5 + 123;
const double eps = 1e-6;
const int inf = (int)1e9 + 123;

using namespace std;

bool u[10];
int n, cnt;
ll nw;

void solve(int test) {
	memset(u, 0, sizeof u);
	cnt = 1;
	scanf("%d", &n);
	while(1) {
		if (cnt > (int)1e6) {
			printf("Case #%d: INSOMNIA\n", test);
			return;
		}
		nw = 1ll * n * cnt;
		while(nw) {
			u[nw % 10] = 1;
			nw /= 10;
		}
		bool ok = 1;
		for (int i = 0; i < 10; i++)
			if (!u[i]) {
				ok = 0;
				break;
			}
		if (ok) {
			printf("Case #%d: %I64d\n", test, 1ll * n * cnt);
			return;
		}
		cnt++;
	}
}

int main() {
	#ifdef Nick
	freopen(fname"in","r",stdin);
	freopen(fname"out","w",stdout);
	#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		solve(i);
	return 0;
}
