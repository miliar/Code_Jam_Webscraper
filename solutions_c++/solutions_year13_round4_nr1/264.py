#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const long long modulo = 1000002013LL;

long long calc(long long N, long long d) {
	//N + (N - 1) .. + (N - d)
	if (d % 2 == 1)
		return (N + (1 - d) / 2) * d % modulo;
	else return (d / 2 * ((N - d + 1 + N) % modulo)) % modulo;
}

int main() {
	int T, N, M;
	cin >> T;
	for (int tcase = 1; tcase <= T; ++ tcase) {
		cin >> N >> M;
		vector< pair<int, long long> > state;
		long long origin_ticket = 0;
		for (int i = 0; i < M; ++ i) {
			int o, e, p;
			cin >> o >> e >> p;
			(origin_ticket += calc(N, e - o) * p) %= modulo;
			state.push_back(make_pair(o, p));
			state.push_back(make_pair(e, -p));
		}
		sort(state.begin(), state.end());
		priority_queue< pair<int, long long> > Q;
		vector< pair<int, long long> >::iterator it = state.begin();
		//cout << "Origin: " << origin_ticket << endl;
		long long current_ticket = 0;
		while (it != state.end()) {
			long long curr = it->second; 
			int timestamp = it->first;
			//cout << "haha" << endl;
			for (++ it; it != state.end() && it->first == timestamp; ++ it) 
				curr += it->second;
			//cout << curr << endl;
			if (curr > 0) {
				Q.push(make_pair(timestamp, curr));
			//	cout << "Push: " << timestamp << "," << curr<< " : " << current_ticket << endl;
			} else {
			//	cout << "Pop: " << timestamp << "," << curr << " : " << current_ticket << endl;
				while (curr != 0) {
					pair<int, long long> top = Q.top();
			//		cout << "curr: " << curr << endl;
			//		cout << "top: " << top.first << ' ' << top.second << endl;
					Q.pop();
					long long pp = min(top.second, -curr);
			//		cout << "pp: " << pp << endl;
					(current_ticket += calc(N, timestamp - top.first) * pp) %= modulo;
					top.second -= pp;
					curr += pp;
					if (top.second > 0)
						Q.push(top);
			//		cout << "hehe" << endl;
				}
			}
		}
		long long diff = (origin_ticket - current_ticket + modulo) % modulo;
		cout << "Case #" << tcase << ": " << diff << endl;
	}
	return 0;
}
