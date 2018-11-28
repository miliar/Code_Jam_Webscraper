#include <cstdio>
#include <cassert>
using namespace std;

const int maxn = 100;
const int maxm = 100;

char a[maxn][maxm];
bool safe_l[maxn][maxm];
bool safe_r[maxn][maxm];
bool safe_u[maxn][maxm];
bool safe_d[maxn][maxm];

void solve()
{
	int n, m;
	scanf("%i%i", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("\n");
		for (int j = 0; j < m; j++) {
			scanf("%c", &a[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		bool ql = false;
		for (int j = 0; j < m; j++) {
			safe_l[i][j] = ql;
			if ('.' != a[i][j])
				ql = true;
		}
		bool qr = false;
		for (int j = m; j; --j) {
			safe_r[i][j -1] = qr;
			if ('.' != a[i][j -1])
				qr = true;
		}
	}
	for (int j = 0; j < m; j++) {
		bool qu = false;
		for (int i = 0; i < n; i++) {
			safe_u[i][j] = qu;
			if ('.' != a[i][j])
				qu = true;
		}
		bool qd = false;
		for (int i = n; i; --i) {
			safe_d[i -1][j] = qd;
			if ('.' != a[i -1][j])
				qd = true;
		}
	}
	int cnt = 0;
	bool impossible = false;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			switch (a[i][j]) {
				break;case '<':
					if (safe_l[i][j]) ;
					else if (false
						|| safe_l[i][j]
						|| safe_r[i][j]
						|| safe_u[i][j]
						|| safe_d[i][j]) cnt++;
					else impossible = true;
				break;case '>':
					if (safe_r[i][j]) ;
					else if (false
						|| safe_l[i][j]
						|| safe_r[i][j]
						|| safe_u[i][j]
						|| safe_d[i][j]) cnt++;
					else impossible = true;
				break;case '^':
					if (safe_u[i][j]) ;
					else if (false
						|| safe_l[i][j]
						|| safe_r[i][j]
						|| safe_u[i][j]
						|| safe_d[i][j]) cnt++;
					else impossible = true;
				break;case 'v':
					if (safe_d[i][j]) ;
					else if (false
						|| safe_l[i][j]
						|| safe_r[i][j]
						|| safe_u[i][j]
						|| safe_d[i][j]) cnt++;
					else impossible = true;
				break;case '.':
				break;default:
					assert(0);
			}
		}
	}
	if (impossible) {
		printf("IMPOSSIBLE");
	}
	else {
		printf("%i", cnt);
	}
}

int main()
{
	int t;
	scanf("%i", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%i: ", i +1);
		solve();
		printf("\n");
	}
	return 0;
}

