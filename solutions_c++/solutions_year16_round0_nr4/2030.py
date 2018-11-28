#include <iostream>
#include <vector>
#define min(a,b) ((a)<(b)?(a):(b))
#define ll long long
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++ icase) {
		cout << "Case #" << icase << ":";
		ll K, C, S;
		cin >> K >> C >> S;
		vector<ll> res;
		vector<bool> vis(K+1, false);
		for (int i = 1; i <= K; ++ i) {
			if (!vis[i]) {
				int cur = i;
				ll pos = i;
				for (int j = 1; j <= C; ++ j) {
					vis[cur] = true;
					if (j == C) res.push_back(pos);
					cur = min(cur+1, K);
					pos = (pos - 1) * K + cur;
				}
			}
		}
		if (res.size() > S) {
			cout << " IMPOSSIBLE" << endl;
			continue;
		}
		for (int i = 0; i < res.size(); ++ i) {
			cout << " " << res[i];
		}
		cout << endl;
	}
	return 0;
}
