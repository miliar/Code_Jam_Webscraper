#include <bits/stdc++.h>

using namespace std;

#define long long long
#define e first
#define f second

vector<pair<long, long>> s;
long neg;
vector<long> ans;


void read() {
	int p;
	cin >> p;
	s.resize(p);
	for (int i = 0; i < p; ++i) 
		cin >> s[i].e;
	for (int i = 0; i < p; ++i)
		cin >> s[i].f;

	sort(s.begin(), s.end());
	neg = -s[0].e;
	for (auto &c : s)
		c.e += neg;

}

void divide(long x) {
	vector<pair<long, long>> ns;
	bool in_neg = false;
	for (int i = 0, j = 0; i < (int) s.size(); ++i) {
		if (s[i].f == 0)
			continue;
		while (j < (int) s.size() && s[j].e < s[i].e + x)
			++j;

		assert(j < (int) s.size());
		assert(s[j].f >= s[i].f);
		assert(s[j].e == s[i].e + x);

		if (!in_neg && s[j].e == neg) {
			in_neg = true;
			neg = s[i].e;
		}

		s[j].f -= s[i].f;
	}

	if (in_neg)
		ans.push_back(-x);
	else
		ans.push_back(x);

	for (auto c : s) 
		if (c.f != 0)
			ns.push_back(c);
	s = ns;
}

void kill() {
	ans.clear();
	while (s.size() > 1) {
		divide(s[1].e);
	}
	while (s[0].f > 1) {
		ans.push_back(0);
		s[0].f /= 2;
	}
	sort(ans.begin(), ans.end());
	for (auto x : ans)
		cout << x << " ";
	cout << "\n";
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		read();
		kill();
		//cerr << "Test #" << i << " done.\n";
	}
	return 0;
}