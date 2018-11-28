#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const int N = (int) 2e6;

int n;
pair <int, int> go[] = {{0, 2}, {0, 1}, {1, 2}};
int ans[N], d[N];
char t[] = {'R', 'P', 'S'};
int a[3];

void cmp(int l, int r, int d) {
	string a, b;
	int m = (l+r) / 2;
	for (int i = l; i <= m; ++i) {
		a += ans[i];
	}
	for (int i = m+1; i <= r; ++i) {
		b += ans[i];
	}
	if (a > b) {
		for (int i = 0; i < d; ++i) {
			swap(ans[l + i], ans[m + i + 1]);
		}
	}
}

void build(int l, int r, int id) {
	if (l == r) {
		ans[l] = t[id];
		a[id]--;
	} else {
		int m = (l + r) / 2;
		build(l, m, go[id].first);
		build(m+1, r, go[id].second);
		cmp(l, r, m-l+1);
	}
}

void init() {
	for (int i = 0; i < 3; ++i) {
		a[i] = d[i];
	}
}

void solve(int test) {
	cin >> n >> d[0] >> d[1] >> d[2];
	cout << "Case #" << test << ": ";
	set <string> s;
	for (int j = 0; j < 3; ++j) {
		init();
		build(0, (1 << n) - 1, j);
		bool good = true;
		for (int i = 0; i < 3; ++i) {
			if (a[i] != 0) {
				good = false;
			}
		}
		if (good) {
			string g;
			for (int i = 0; i < (1 << n); ++i) {
				 g += (char)ans[i];
			}
			s.insert(g);
		}
	}
	if (s.empty())
		cout << "IMPOSSIBLE\n";
	else {
		cout << *s.begin() << '\n';
	}
}


int main()
{
	ios_base::sync_with_stdio(0);
#ifdef KOBRA
	freopen("testor", "r", stdin);
	freopen("output", "w", stdout);
#else
//	freopen("minimization.in", "r", stdin);
//	freopen("minimization.out", "w", stdout);
#endif // KOBRA
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; ++i) {
		solve(i);
//		stress();
	}
	return 0;
}

