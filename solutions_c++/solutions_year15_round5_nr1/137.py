#include <bits/stdc++.h>

#define itn itn
#define all(x) (x).begin(), (x).end()
#define x first
#define y second

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

void solve(){
	int n = nxt();
	int d = nxt();
	vector<int> s(n), m(n);
	int as, cs, rs, am, cm, rm;
	s[0] = nxt();
	as = nxt();
	cs = nxt();
	rs = nxt();
	m[0] = nxt();
	am = nxt();
	cm = nxt();
	rm = nxt();
	for (int i = 0; i < n - 1; i++){
		s[i + 1] = (1ll * s[i] * as + cs) % rs;
		m[i + 1] = (1ll * m[i] * am + cm) % rm;
	}
	for (int i = 1; i < n; i++)
		m[i] %= i;
	vector<vector<int>> a(n);
	for (int i = 1; i < n; i++)
		a[m[i]].push_back(i);
	vector<char> used(n);
	vector<pair<int, int>> emp(n);
	for (int i = 0; i < n; i++)
		emp[i] = {s[i], i};
	sort(all(emp));
	int l = 0, r;
	while (emp[l].x < s[0] - d)
		l++;
	r = l;
	int cnt = 1;
	int ans = 1;
	used[0] = 1;
	vector<int> cn(n);
	cn[0] = 1;
	while (r < n && emp[r].x <= s[0] + d){
		if (emp[r].y == 0){
			r++;
			continue;
		}
		int v = emp[r].y;
		used[v] = 1;
		cn[v] = 1;
		for (auto x : a[v])
			if (used[x])
				cn[v] += cn[x];
		int ad = cn[v];
		while (v > 0 && used[m[v]]){
			cn[m[v]] += ad;
			v = m[v];
		}
		if (v == 0)
			cnt += ad;
		while (emp[r].x > emp[l].x + d){
			int v = emp[l].y;
			used[v] = 0;
			int ad = cn[v];
			cn[v] -= ad;
			while (v > 0 && used[m[v]]){
				cn[m[v]] -= ad;
				v = m[v];
			}
			if (v == 0)
				cnt -= ad;
			l++;
		}
		ans = max(ans, cnt);
		r++;
	}
	printf("%d\n", ans);
}

int main(){

	int T = nxt();
	for (int _ = 0; _ < T; _++){
		printf("Case #%d: ", _ + 1);
		solve();
		cerr << "Test #" << _ + 1 << " completed\n";
	}

	return 0;
}