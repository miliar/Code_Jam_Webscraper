#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define bits(x) __builtin_popcount(x)
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

#define MOD 1000002013

long long N, from, to;
int pas;

int main() {
	int casos, M;

	cin>>casos;
	for (int caso = 1; caso <= casos; caso++) {
		cin>>N>>M;
		long long menos=0;
		vector<pair<long long, pair<int, int> > > events;
		for (int i=0;i<M;i++) {
			cin>>from>>to>>pas;
			long long dif = to-from;
			long long tt = ((dif*(dif+1))/2) % MOD;
			tt*=pas;
			menos += tt;
			menos %= MOD;
			events.push_back(make_pair(from, make_pair(0, pas)));
			events.push_back(make_pair(to, make_pair(1, pas)));
		}
		sort(all(events));
		long long maxmenos = 0;
		stack<pair<long long, int> > tengo;
		for (int i=0;i<(int)events.size();i++) {
			if (events[i].second.first == 0) {
				tengo.push(make_pair(events[i].first, events[i].second.second));
			} else {
				int des=events[i].second.second;
				long long current = events[i].first;
				while (des > 0) {
					pair<long long, int> &cu = tengo.top();
					int saca = min(des, cu.second);
					long long ddd = current - cu.first;
					long long val = (ddd*(ddd+1) / 2) %MOD;
					maxmenos += val * saca;
					maxmenos %= MOD;
					cu.second -= saca;
					des -= saca;
					if (cu.second == 0) tengo.pop();
				}
			}
		}
		long long ans = (maxmenos +MOD - menos) % MOD;
		cout << "Case #" << caso << ": " << ans << endl;
	}
	return 0;
}
