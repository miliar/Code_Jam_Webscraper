#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

long long MOD = 1000002013;

struct Event {
	int point;
	long long cost;
};
bool operator<(Event a, Event b) {
	return a.point < b.point;
}

long long Cost(int N, int len, long long howmany) {
	long long len2 = len;
	long long c = (len2 * N - (len2 * (len2-1)) / 2) % MOD;
	return (c * (howmany % MOD));
}

long long solve() {
	int N, M;
	cin >> N >> M;
	vector<Event> ev, ev2;
	long long origcost = 0;
	for (int i = 0; i < M; ++i) {
		Event e;
		int start, end, cost;
		cin >> start >> end >> cost;
		origcost += Cost(N, end - start, cost);
		origcost %= MOD;
		e.point = start;
		e.cost = cost;
		ev.push_back(e);
		e.cost = -cost;
		e.point = end;
		ev.push_back(e);
	}
	sort(ev.begin(), ev.end());
	for (int i = 0; i < (int)ev.size(); ++i) {
		if (!ev2.empty() && ev2.back().point == ev[i].point) {
			ev2.back().cost += ev[i].cost;
		}
		else
			ev2.push_back(ev[i]);
	}
	ev.swap(ev2);

	long long totcost = 0;
	bool changed = true;
	int sz = (int)ev.size();
	while (changed) {
		changed = false;
		for (int i = 0; i < sz; ++i) {
			if (ev[i].cost) {
				changed = true;
				long long now = ev[i].cost, min = now;
				for (int j = i+1; j < sz; ++j) {
					now += ev[j].cost;
					if (!now) {
						// Done, from ev[i].point to ev[j].point decrease min
						ev[i].cost -= min;
						ev[j].cost += min;
						int len = ev[j].point - ev[i].point;
						totcost += Cost(N, len, min);
						totcost %= MOD;
						break;
					}
					else if (now < min)
						min = now;
				}
				break;
			}
		}
	}

	return (origcost - totcost + MOD) % MOD;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
}
