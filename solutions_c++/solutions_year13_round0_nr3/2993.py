#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
	long long v, s;
	Node(long long  vv, long long ss) : v(vv), s(ss) {}
	bool operator<(const Node &a) const {
		return this->s < a.s;
	}
};

vector<Node> res;

bool is_palind(long long v) {
	string s = "";
	while (v) {
		s += v % 10 + '0';
		v /= 10;
	}
	for (int i = 0; i < s.length() / 2; i++)
		if (s[i] != s[s.length() - i - 1]) return false;

	return true;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	for (int i = 1; i < 1000; i++) {
		long long v = i;
		long long t = i / 10;
		while (t) { // odd
			v = v * 10 + t % 10;
			t /= 10;
		}
		if (is_palind(v * v)) res.push_back(Node(v, v * v));
		
		v = i;
		t = i;
		while (t) { // even
			v = v * 10 + t % 10;
			t /= 10;
		}
		if (is_palind(v * v)) res.push_back(Node(v, v * v));
	}
	sort(res.begin(), res.end());

	/*
	cout << res.size() << '\n';
	for (int i = 0; i < res.size(); i++)
		cout << res[i].v << ' ' << res[i].s << '\n';
	cout << '\n';
	*/

	int T;
	cin >> T;
	long long a, b;
	for (int  cas = 1; cas <= T; cas++) {
		cin >> a >> b;
		cout << "Case #" << cas << ": " << upper_bound(res.begin(), res.end(), Node(-1, b)) - lower_bound(res.begin(), res.end(), Node(-1, a)) << '\n';
	}

	// system("pause");
	return 0;
}