#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
#define REP(i, n) for (int i = 0; i < n; ++i)
#define PB push_back
#define MP make_pair
typedef long long ll;

const ll MOD = 1000002013ll;

struct Node
{
	int pos;
	int state;
	int num;
	Node(int _pos, int _state, int _num) : pos(_pos), state(_state), num(_num) {

	}
	bool operator < (const Node &a) const {
		return pos < a.pos || (pos == a.pos && state < a.state);
	}
};
ll n;
int m;
ll dist(ll x) {
	return (n + n-x+1) * x / 2 % MOD;
}
int main() {
	int test;
	int a, b, c;
	cin >> test;
	for (int cas = 1; cas <= test; ++cas) {
		cin >> n >> m;
		ll old = 0;
		vector<Node> events;
		REP(i, m) {
			cin >> a >> b >> c;
			events.push_back(Node(a, 0, c));
			events.push_back(Node(b, 1, c));
			old = old + dist(b-a) * c;
		}
		sort(events.begin(), events.end());

		vector<pair<int,int> > left;
		ll ans = 0;
		REP(i, events.size()) {
			int state = events[i].state;
			int pos = events[i].pos;
			int num = events[i].num;
			if (state == 1) {
				int leave = num;
				while (leave > 0) {
					ll go = min(left.back().second, leave);
					ans = (ans + dist(pos - left.back().first) * go % MOD) % MOD;
					//cout << "ans = " << ans << endl;
					left.back().second -= go;
					leave -= go;
					if (left.back().second == 0) left.pop_back();
				}
			} else {
				left.push_back(make_pair(pos, num));
			}
		}
		//cout << old << " " << ans << endl;
		ans = (old - ans) % MOD;
		ans = (ans + MOD) % MOD;
		cout << "Case #" << cas << ": " << ans << endl;
	}
}




