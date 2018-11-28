#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef pair<ll, ii> iii;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;

const int inf = 1e9;

int find_first(string s) {
	for (int i = 0; i < s.size(); i++)
		if (s[i] == '?')
			return i;
	return -1;
}

ll toint(string s) {
	ll ret = 0;
	for (int i = 0; i < s.size(); i++)
		ret = ret * 10 + s[i] - '0';
	return ret;
}

void all(string a, vi& ret) {
	int q = find_first(a);
	if (q == -1) {
		ret.push_back(toint(a));
		return;
	}
	for (int i = 0; i < 10; i++) {
		a[q] = i + '0';
		all(a, ret);
		a[q] = '?';
	}
}

bool comp(iii a, iii b) {
	if (a.first == b.first) {
		if (a.second.first == b.second.first)
			return a.second.second < b.second.second;
		return a.second.first < b.second.first;
	}
	return a.first < b.first;
}

int main() {
	ios::sync_with_stdio(false);

	int ts; cin >> ts;
	for (int t = 1; t <= ts; t++) {
		string a, b;
		cin >> a >> b;
		vi first, second;
		all(a, first);
		all(b, second);
		// if (find_first(a) == -1)
		// 	first.push_back(toint(a));
		// if (find_first(b) == -1)
		// 	second.push_back(toint(b));
		viii together;
		for (int i = 0; i < first.size(); i++)
			for (int j = 0; j < second.size(); j++) {
				together.push_back(iii(abs(first[i] - second[j]), ii(first[i], second[j])));
				// cerr << abs(together.back().second.first - together.back().second.second) << endl;
			}
		sort(together.begin(), together.end(), comp);
		// for (int i = 0; i < together.size(); i++)
			// cerr << together[i].first << ' ' << together[i].second.first << ' ' << together[i].second.second << endl;
		cout << "Case #" << t << ": " <<
			setfill('0') << setw(a.size()) << together[0].second.first << ' ' <<
			setfill('0') << setw(a.size()) << together[0].second.second << endl;
	}

	return 0;
}
