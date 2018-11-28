#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <stdio.h>

using namespace std;

using ll = long long;
using ull = unsigned long long;
template<typename T> using vv = vector<vector<T>>;
using pii = pair<int, int>;
using pll = pair<long long, long long>;

inline ll nl() { ll n; scanf("%I64d ", &n); return n; }
inline int ni() { int n; scanf("%d ", &n); return n; }
vector<int> v;

struct point {
	ll x, y;
};

vector<point> pt;

double psevdo(point a, point b, point c) {
	return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

double R(point a, point b) {
	return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}


vector<point> get_hull(vector<point> &pt) {
	point first = { (ll)1e9, (ll)1e9 };

	for (auto p : pt) {
		if (p.x < first.x || (p.x == first.x && p.y < first.y)) {
			first = p;
		}
	}

	sort(pt.begin(), pt.end(), [&](point a, point b) {return (psevdo(first, a, b) > 0 || 
								  (psevdo(first, a, b) == 0 && R(first, a) < R(first, b)));});
	vector<point> res;

	int n = pt.size();

	res.push_back(pt[0]), res.push_back(pt[1]);

	for (int i = 2; i < n; ++i) {
		point cur = res.back();
		point next = pt[i];
		point prev = res[res.size() - 2];
		while (res.size() >= 2 && psevdo(cur, next, prev) <= 0) {
			res.pop_back();
			cur = res.back();
			if (res.size() >= 2) {
				prev = res[res.size() - 2];
			}
		}
		res.push_back(next);
	}

	return res;

}

vector<int> get_dig(ll a) {
	vector<int> res;
	while (a > 0) {
		res.push_back(a % 10);
		a /= 10;
	}

	return res;
}

//#define LOCAL

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#else
#define task "hull"
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	cin.tie(0);
	int n;
	cin >> n;

	for (int i = 0; i < n; ++i) {
		ll x;

		cin >> x;
		cout << "Case #" << i + 1 << ": ";
		if (!x) {
			cout << "INSOMNIA" << endl;
			continue;
		}

		ll j = 1;

		set<int> dig;

		while (1) {
			auto v = get_dig(x * j);
			for (auto a : v) {
				dig.insert(a);
			}

			if (dig.size() == 10) {
				cout << x * j << endl;
				break;
			}

			++j;
		}
	}

}