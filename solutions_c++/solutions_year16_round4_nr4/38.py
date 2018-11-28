/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define zero(a) memset(a, 0, sizeof(a))

typedef pair <int, int> pii;

int n, cnt1, cnt2;
vector<string> s;
vector<int> u1, u2;

void dfs2( int v );
void dfs1( int v ) {
	u1[v] = 1, cnt1++;
	forn(i, n) 
		if (!u2[i] && s[v][i] == '1')
			dfs2(i);
}
void dfs2( int v ) {
	u2[v] = 1, cnt2++;
	forn(i, n) 
		if (!u1[i] && s[i][v] == '1')
			dfs1(i);
}

const int N = 25;
const int K = 16;

int f[1 << K][N][N];

inline void relax( int &a, int b ) { a = min(a, b); }

void solve() {
	cin >> n;
	s.resize(n);
	u1 = u2 = vector<int>(n, 0);
	int one = 0;
	forn(i, n) {
		cin >> s[i];
		forn(j, n)
			one += (s[i][j] == '1');
	}
		
	int free1 = 0, free2 = 0, add = 0;
	vector<pii> v;
	forn(i, n)
		if (!u1[i]) {
			cnt1 = cnt2 = 0;
			dfs1(i);
			if (!cnt2)
				free1++;
			else if (cnt1 != cnt2)
				v.push_back(pii(cnt1, cnt2));
			else
				add += cnt1 * cnt2;
		}
	forn(i, n)
		if (!u2[i])
			free2++;
	int k = v.size();
	fprintf(stderr, "solve k = %d, free = %d %d\n", k, free1, free2);
	fprintf(stderr, "time = %.2f\n", 1. * clock() / CLOCKS_PER_SEC); // stamp

	assert(k <= K);
	memset(f, 0x3F, sizeof(f));
	f[0][0][0] = 0;
	forn(j, 1 << k) if (j) {
		int a = 0, b = 0;
		forn(t, k)
			if ((j >> t) & 1) {
				a += v[t].first;
				b += v[t].second;
			}
		int add1 = max(0, b - a);
		int add2 = max(0, a - b);
		int df = max(a, b);
		df *= df;
		for (int i = j; i < (1 << k); i++, i |= j)
			forn(f1, free1 - add1 + 1)
				forn(f2, free2 - add2 + 1)
					relax(f[i][f1 + add1][f2 + add2], f[i ^ j][f1][f2] + df);
	}
	int best = n * n;
	forn(rest, free1 + 1)
		relax(best, f[(1 << k) - 1][free1 - rest][free2 - rest] + rest);
	printf("%d\n", best + add - one);		 
}

int main() {
  int n;
  scanf("%d ", &n);
  for (int i = 1; i <= n; i++) {
    printf("Case #%d: ", i);
    solve();
  }
}
