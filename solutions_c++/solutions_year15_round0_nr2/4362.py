#include <bits/stdc++.h>

using namespace std;

int t;

ifstream in("pancakes.in");
ofstream out("pancakes.out");

int main ()
{
	in >> t;
	for (int i = 0; i ++< t;) {
		int d, p, m = 1e9;
		in >> d;
		vector<int> v;
		map<vector<int>, int> o;
		for (int j = 0; j < d; ++j) in >> p, v.push_back(p);
		sort(v.begin(), v.end());
		queue<pair<vector<int>, int>> q;
		o[v] = 0;
		q.emplace(v, 0);
		while (q.size()) {
			v = q.front().first, p = q.front().second; q.pop();
			if (p > 9) continue;
			for (int i = v.size(); i --> 0;) if (v[i]) goto c;
			m = min(m, p);
			continue;
c:
			int i = v.size() - 1;
			for (int c = 1; c <= v[i]; ++c) {
				for (int j = v.size(); j --> 0;) if (i != j) {
					if (v[j] + c >= v[i] - c) continue;
					auto u = v;
					u[i] -= c, u[j] += c;
					sort(u.begin(), u.end());
					if (!o.count(u) || p + 1 < o[u]) q.emplace(u, o[u] = p + 1);
				}
				auto u = v;
				u[i] -= c;
				u.push_back(c);
				sort(u.begin(), u.end());
				if (!o.count(u) || p + 1 < o[u]) q.emplace(u, o[u] = p + 1);
			}
			for (int i = v.size(); i --> 0;) v[i] = max(v[i] - 1, 0);
			sort(v.begin(), v.end());
			if (!o.count(v) || p + 1 < o[v]) q.emplace(v, o[v] = p + 1);
		}
		out << "Case #" << i << ": " << m << '\n';
		cout << "Case #" << i << ": " << m << '\n';
	}
}

