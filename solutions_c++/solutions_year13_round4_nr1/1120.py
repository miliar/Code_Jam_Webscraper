#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <numeric>

using namespace std;

#define MOD 1000002013

map<int, long long> distanceBefore, distanceAfter;
set<pair<int, int> > ps;
int N, M;
int journeys[1010][3];
map<int, vector<int> > entry, leave;


void read() {
	distanceBefore.clear();
	distanceAfter.clear();
	ps.clear();
	entry.clear();
	leave.clear();
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%d", &journeys[i][j]);
		}
		distanceBefore[journeys[i][1] - journeys[i][0]] += journeys[i][2];
		ps.insert(make_pair(journeys[i][0], -1));
		ps.insert(make_pair(journeys[i][1], 0));
		if (entry.count(journeys[i][0]) == 0) {
			entry.insert(make_pair(journeys[i][0], vector<int>()));
		}
		entry[journeys[i][0]].push_back(i);
		if (leave.count(journeys[i][1]) == 0) {
			leave.insert(make_pair(journeys[i][1], vector<int>()));
		}
		leave[journeys[i][1]].push_back(i);
	}
}

void process() {
	// lembrar de sempre fazer operações envolvendo LL
	vector<pair<int, int> > heap;
	vector<pair<int, int> >points(ps.begin(), ps.end());
	for (int i = 0; i < points.size(); i++) {
		if (points[i].second) {
			vector<int> &v = entry[points[i].first];
			for (int j = 0; j < v.size(); j++) {
				int idx = v[j];
				heap.push_back(make_pair(idx, journeys[idx][2]));
			}
		} else {
			vector<int> &v = leave[points[i].first];
			for (int j = 0; j < v.size(); j++) {
				int idx = v[j];
				int amount = journeys[idx][2];
				while (amount > 0) {
					if (heap.empty()) {
						while(1);
					}
					pair<int, int> tmp = heap[heap.size() - 1];
					heap.pop_back();
					if (tmp.second <= amount) {
						distanceAfter[points[i].first - journeys[tmp.first][0]] += tmp.second;
						amount -= tmp.second;
					} else {
						tmp.second -= amount;
						distanceAfter[points[i].first - journeys[tmp.first][0]] += amount;
						amount = 0;
						heap.push_back(tmp);
					}
				}
			}
		}
	}
	long long answ = 0;
	for (map<int, long long>::iterator it = distanceBefore.begin(); it != distanceBefore.end(); it++) {
		it->second %= MOD;
		long long a = 2LL * N - it->first - 1;
		long long b = it->first;
		if (a % 2 == 0) {
			a /= 2;
		} else {
			b /= 2;
		}
		a %= MOD;
		b %= MOD;
		answ = (answ + (a * b) * it->second) % MOD;
	}
	long long newValue = 0;
	for (map<int, long long>::iterator it = distanceAfter.begin(); it != distanceAfter.end(); it++) {
		it->second %= MOD;
		long long a = 2LL * N - it->first - 1;
		long long b = it->first;
		if (a % 2 == 0) {
			a /= 2;
		} else {
			b /= 2;
		}
		a %= MOD;
		b %= MOD;
		newValue = (newValue + ((a * b) % MOD) * it->second) % MOD;
	}

	answ = (answ - newValue + MOD) % MOD;
	printf("%lld\n", answ);	
}

int main() {
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}