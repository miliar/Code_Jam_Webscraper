#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

const long long MOD = 1000002013;

int t1, t2, t3;
long long n, m, cost1, cost2;
vector<pair<int, int> > evt; 
priority_queue<pair<int, int> > heap;

long long cal(long long a) {
	return ((2 * n - a + 1) * a / 2) % MOD;
}

bool cmp(const pair<int, int> a, const pair<int, int> b) {return a.first < b.first || a.first == b.first && a.second > b.second;}

int main() {
	freopen("A-Large.in", "r", stdin);
	freopen("A-L.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int V = 1; V <= T; ++V) {
		evt.clear();
		cin >> n >> m;
		long long cost1 = 0, cost2 = 0;
		for (int i = 1; i <= m; ++i) {
		  scanf("%d %d %d", &t1, &t2, &t3);
		  cost1 = (cost1 + (t3 * cal(t2 - t1)) % MOD) % MOD;
		  evt.push_back(make_pair(t1, t3));
		  evt.push_back(make_pair(t2, -t3));
		}
		while (heap.size()) heap.pop();
		sort(evt.begin(), evt.end(), cmp);
		for (int i = 0; i < evt.size(); ++i) {
		  if (evt[i].second > 0) {
		    heap.push(evt[i]);
			} else {
				pair<int, int> tmp;
				while (evt[i].second < 0) {
				  tmp = heap.top();
				  heap.pop();
 				  int pep = min(-evt[i].second, tmp.second);
				  evt[i].second += tmp.second;
				  tmp.second -= pep;
				  cost2 = (cost2 + (pep * cal(evt[i].first - tmp.first)) % MOD) % MOD;
				}
				if (tmp.second > 0) heap.push(tmp);
		  }
		}
		long long ans = cost1 - cost2;
		if (ans < 0) ans += MOD;
	  cout << "Case #" << V << ": " << ans << endl;
	}
	return 0;
}

