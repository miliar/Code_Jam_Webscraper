#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>

using namespace std;

const int maxn = 1010;
bool seen[maxn], cycStart[maxn];
int to[maxn];
vector<int> prev[maxn];
int n, t, ans, mx;

inline void setmax(int &a, int b) {if (a < b) a = b; }

void backTrack(int cur, int depth) {
	setmax(mx, depth);
	for (int i = 0; i < prev[cur].size(); i++) {
		if (prev[cur][i] == to[cur]) continue;
		backTrack(prev[cur][i], depth+1);
	}
}

void checkCyc(int i) {
	memset(seen, 0, sizeof(seen));
	int start = i, cnt = 0;
	while (!seen[i]) {
		seen[i] = true;
		i = to[i];
		cnt++;
	}
	if (i != start) return;
	setmax(ans, cnt);
}

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("C.in");
	ofstream cout("C.out");
	cin >> t;
	for (int rep = 1; rep <= t; rep++) {
		memset(cycStart, 0, sizeof(cycStart));
		cout << "CASE #" << rep << ": ";
		cin >> n;
		ans = 0;
		for (int i = 0; i < n; i++) {
			prev[i].clear();
		}
		for (int i = 0; i < n; i++) {
			cin >> to[i];
			to[i]--;
			prev[to[i]].push_back(i);
		}
		for (int i = 0; i < n; i++) {
			if (to[to[i]] == i) {
				backTrack(i, 1);
				ans += mx;
				mx = 0;
			}
		}
		for (int i = 0; i < n; i++) {
			checkCyc(i);
		}
		cout << ans << endl;
	}
	return 0;
}

