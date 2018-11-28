#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
map<ll, ll> v;
queue<ll> q;
int nt, it;
ll n[100], o[100];
bool done = false;
const ll inf = 1E18;

vi to_vi(ll x) {
	vi s;

	while (x) {
		s.push_back(x % 10);
		x /= 10;
	}

	return s;
}

ll to_ll(vi v) {
	ll r = 0;

	for (int i = v.size(); i--; ) r = r * 10 + v[i];

	return r;
}

void mark() {
	done = true;

	for (it = 0; it < nt; it++) if (o[it] == 1E14) {
		if (v.find(n[it]) != v.end()) {
			o[it] = v[n[it]];
		}
		if (o[it] == 1E14) {
			done = false;
		}
	}
}

void visit(ll s, ll d) {
	if (v.find(s) == v.end()) {
		// cout << s << ' ' << p.first << ' ' << p.second << endl;
		v[s] = d;
		q.push(s);
		if (v.size() % 100 == 0) mark();
	}
}

int main() {
	cin >> nt;

	for (it = 0; it < nt; it++) {
		cin >> n[it];
		o[it] = 1E14;
	}

	visit(1, 1);
	while (!done && q.size()) {
		ll s = q.front(); q.pop();
		ll d = v[s];

		if (s < inf && s > -inf) {
			visit(s + 1, d + 1);

			vi t = to_vi(s);

			reverse(t.begin(), t.end());
			visit(to_ll(t), d + 1);
		}
	}

	for (it = 0; it < nt; it++) {
		cout << "Case #" << it + 1 << ": " << o[it] << endl;
	}
}
