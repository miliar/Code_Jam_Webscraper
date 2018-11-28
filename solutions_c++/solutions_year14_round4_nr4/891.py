#include <iostream>
#include <cstdio>
#include <fstream>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <cstring>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <memory.h>
using namespace std;

#define fr(i, n) for (int i = 0; i < (int)(n); i++)
#define fb(i, n) for (int i = n - 1; i >= 0; i--)
#define all(a) (a).begin(), (a).end()
#define _(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline int ni() { int a; scanf("%d", &a); return a; }
inline double nf() { double a; scanf("%lf", &a); return a; }
template <class T> void out(T a, T b) { bool first = true; for (T i = a; i != b; i++) { if (!first) printf(" "); first = false; cout << *i; } puts(""); }
template <class T> void outl(T a, T b) { for (T i = a; i != b; i++) cout << *i << "\n"; } 

const int MOD = 1000000007;
const int MAXN = 26;
const int MAXM = 10000;

struct node {
	int next[MAXN];
};

node d[MAXM];
int dsz;

int T;
int M, N;
vs v;

bool next(vi &cur) {
	int pos = M - 1;
	cur[pos]++;
	while (pos > 0 && cur[pos] == N) {
		cur[pos--] = 0;
		cur[pos]++;
	}
	return !(pos == 0 && cur[pos] == N);
}

void add(string &s) {
	int cur = 0;
	fr(j, sz(s)) {
		if (d[cur].next[s[j] - 'A'] == -1)
			d[cur].next[s[j] - 'A'] = dsz++;
		cur = d[cur].next[s[j] - 'A'];
	}
}

pii solve() {
	M = ni();
	N = ni();	
	v.clear();
	v.resize(M);
	fr(i, M)
		cin >> v[i];

	int ans = -1, cans = 0;

	dsz = 0;
	fr(i, MAXM)
		memset(d[i].next, -1, sizeof(d[i].next));

	
	vi cur(M, 0);
	vector<vi> a(N);
	do {
		int c = 0;
		fr(i, N)
			a[i].clear();
		fr(i, M)
			a[cur[i]].pb(i);

		bool flag = false;
		fr(i, N)
			if (sz(a[i]) == 0)
				flag = true;
		if (flag)
			continue;

		fr(i, N) {
			dsz = 1;
			fr(j, sz(a[i]))
				add(v[a[i][j]]);
			c += dsz;
			//dsz = 1;
			for (int j = dsz; j >= 0; j--)
				memset(d[j].next, -1, sizeof(d[j].next));
		}	

		if (c > ans)
			ans = c, cans = 1;
		else if (c == ans)
			cans++;
		
		//out(all(cur));
		//cout << endl;

	} while (next(cur));
	return mp(ans, cans);
}

int main() {
	freopen("triesharding.in", "r", stdin);
	freopen("triesharding.out", "w", stdout);  
	T = ni();
	fr(test, T) {
		pii res = solve();
		printf("Case #%d: %d %d\n", test + 1, res.first, res.second);
	}
}
        