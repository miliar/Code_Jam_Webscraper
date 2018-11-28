#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;

const int Dsize = 128;
map<vector<int>, int> memo;

int findTimeMin(vector<int> &hist) {
	int maxPans = hist[0];
	if (maxPans <= 3) {
		return memo[hist] = maxPans;
	}
	int timeMin = maxPans;
	if (memo.count(hist)) {
		return memo[hist];
	}
	for (int mvPans = 1; mvPans < 1+maxPans/2; mvPans++) {
		hist[maxPans]--;
		hist[mvPans]++;
		hist[maxPans-mvPans]++;
		for (int i = maxPans; i > 0;i--){
			if (hist[i] != 0) {
				hist[0] = i;
				break;
			}
		}
		timeMin = min(timeMin, 1 + findTimeMin(hist));
		hist[maxPans-mvPans]--;
		hist[mvPans]--;
		hist[maxPans]++;
		hist[0] = maxPans;
	}
	return memo[hist] = timeMin;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int D;
		cin >> D;
		vector<int> hist(Dsize, 0);
		for (int i = 0; i < D; i++) {
			int p;
			cin >> p;
			hist[p]++;
			hist[0] = max(hist[0], p);
		}
		int timeMin = findTimeMin(hist);
		printf("Case #%d: %d\n", t, timeMin);
	}
	return 0;
}
