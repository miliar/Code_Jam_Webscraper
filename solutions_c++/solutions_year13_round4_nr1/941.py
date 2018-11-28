#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i, b) FOR(i,0, b)
#define FE(it, set) for(auto& it = (set).begin(); it != (set).end(); it++)

using namespace std;
typedef vector<int> vi;
typedef long long ll;

#define pos first
#define num second
typedef pair<int, int> stop;

ll cost(ll d, ll n) {
	return d * n - (d * (d-1)) / 2;
}
void solve() {
	const ll MOD = 1000002013L;
	int n, m;
	cin >> n >> m;
	vector<stop> origins(m);
	vector<stop> ends(m);
	ll original_cost = 0;
	REP(i, m) {
		int o, e, num;
		cin >> o >> e >> num;
		origins[i] = (stop(o, num));
		ends[i] = (stop(e, num));

		original_cost += cost(e - o, n) * num;
	}

	sort(origins.begin(), origins.end());
	sort(ends.begin(), ends.end());

	priority_queue<stop> startPos;
	int i = 0, j = 0;
	ll cheapest_cost = 0;
	while(j < m) {
		const int cur = min(i < m ? origins[i].pos : n, ends[j].pos);
		//cout << i  << "," << j << "=" << cur<< endl;
		while(i < m && origins[i].pos == cur) {
			startPos.push(origins[i]);
			i++;
		}

		while(j < m && ends[j].pos == cur) {
			stop begin = startPos.top(); startPos.pop();

			const int amount = min(begin.num, ends[j].num);

			//cout << begin.pos << " to " << cur << endl;
			cheapest_cost += amount * cost(cur - begin.pos, n);
			cheapest_cost %= MOD;

			begin.num -= amount;
			ends[j].num -= amount;

			if(begin.num > 0) {
				startPos.push(begin);
			}

			if(ends[j].num == 0) {
				j++;
			}
		}
	}
	//cout << original_cost << " - " << cheapest_cost << " = ";
	ll sol = original_cost - cheapest_cost;
	sol += MOD;
	sol %= MOD;
	cout << sol;
}
// g++0x

int main(int argc, char** argv) {
	int n = 0;
	ios::sync_with_stdio(false);
	cin >> n;

	FOR(i,1,n+1) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
