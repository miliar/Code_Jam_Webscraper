/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define sz(a) (int)(a).size()

typedef double dbl;

inline double gen() {
	return 1. * rand() / RAND_MAX;
}

void solve() {
	int n, m;
	cin >> n;
	vector<int> c[n + 1];
	forn(i, n) {
		int p;
		cin >> p;
		c[p].push_back(i + 1);
	}
	string s;
	cin >> s >> m;
	s = "_" + s;
	string name[m];
	forn(i, m) cin >> name[i];
	
	n++;
	int size[n];
	function<void(int)> calc = [&]( int v ) { 
		size[v] = 1;
		for (int x : c[v]) 
			calc(x), size[v] += size[x];
	};
	calc(0);

	vector<int> roots;
	string str;
	int T = 1e4;
	vector<double> res(m);
	forn(_, T) {
		roots.clear();
		roots.push_back(0);
		str = "";
		while (roots.size()) {
			dbl sum = 0;
			for (int r : roots) sum += size[r];
			sum *= gen();
			int i = 0;
			while (i + 1 < sz(roots) && size[roots[i]] < sum)
				sum -= size[roots[i++]];
			int r = roots[i];
			roots[i] = roots.back();
			roots.pop_back();
			for (int x : c[r]) roots.push_back(x);
			//cout << r << " " << s[r] << "\n";
			str += s[r];	
		}
		forn(i, m)
			res[i] += (strstr(str.c_str(), name[i].c_str()) != 0);
		//cout << str << "\n";
	}
	forn(i, m)
		printf("%.6f%c", res[i] / T, " \n"[i == m - 1]);
}

int main() {
	int n;
	ios_base::sync_with_stdio(0), cin.tie(0);
	cin >> n;
	for (int i = 1; i <= n; i++) {
		fprintf(stderr, "%d of %d\n", i, n);
		printf("Case #%d: ", i);
		//puts("");
		solve();
	}
	fprintf(stderr, "time = %.2f\n", 1. * clock() / CLOCKS_PER_SEC); // stamp
}
