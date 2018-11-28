#include <iostream>
#include <map>

using namespace std;

unsigned long long cost(unsigned long long o, unsigned long long e, unsigned long long N) 
{
	return (2*N-(e-o-1))*(e-o)/2;
}

int main() {
	int T;
	cin >> T;
	for (int t=1; t<=T; ++t) {
		unsigned long long fairCost = 0;
		map<int, int> station2change;
		int N, M;
		cin >> N >> M;
		for (int j=0; j<M; ++j) {
			int o, e, p;
			cin >> o >> e >> p;
			station2change[o] += p;
			station2change[e] -= p;
			fairCost += p * cost(o, e, N);
		}
		unsigned long long fakedCost = 0;
		while (!station2change.empty()) {
			if (station2change.begin()->second == 0) {
				station2change.erase(station2change.begin());
				continue;
			}
			auto cur = station2change.begin();
			int max2remove = cur->second;
			for (int cnt = cur->second; cnt > 0; ) {
				++cur;
				cnt += cur->second;
				if (cnt > 0) max2remove = min(cnt, max2remove);
			}

			station2change.begin()->second -= max2remove;
			cur->second += max2remove;
			fakedCost += max2remove * cost(station2change.begin()->first, cur->first, N);
		}

		cout << "Case #" << t << ": " << (fairCost-fakedCost)%1000002013 << endl;
	}
	return 0;
}