#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <utility>
#include <vector>

using namespace std;

vector<int> chestKeyType;
vector<vector<int> > chestTreasure;
bool calculated;
int numChest;

int visited[1<<21];

vector<int> bt(int mask, map<int,int>& availKeys) {
	vector<int> res;
	visited[mask] = 1;
	if (mask == (1 << numChest)-1) {
		calculated = true;
		return vector<int>();
	}
	for (int i = 0; i < numChest; i++) {
		if (mask & (1 << i)) {
			continue;
		}
		if (availKeys.count(chestKeyType[i]) == 0 || availKeys[chestKeyType[i]] <= 0) {
			continue;
		}
		if (visited[mask | (1 << i)]) {
			continue;
		}
		// backtrack this chest
		map<int,int> copyAvailKeys(availKeys);
		copyAvailKeys[chestKeyType[i]]--;
		// open this treasure
		for (int j = 0; j < chestTreasure[i].size(); j++) {
			copyAvailKeys[chestTreasure[i][j]]++;
		}
		// now run
		vector<int> temp = bt(mask | (1 << i), copyAvailKeys);
		if (calculated) {
			temp.push_back(i);
			return temp;
		}
	}
	return res;
}


int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int K, N; cin >> K >> N;
		calculated = false;
		memset(visited, 0, sizeof(visited));
		map<int,int> availKeys;
		for (int i = 0; i < K; i++) {
			int val; cin >> val; availKeys[val]++;
		}
		numChest = N;
		chestKeyType.clear();
		chestTreasure.clear();
		for (int i = 0; i < N; i++) {
			int Ti, Ki; cin >> Ti >> Ki;
			chestKeyType.push_back(Ti);
			chestTreasure.push_back(vector<int>());
			for (int j = 0; j < Ki; j++) {
				int val; cin >> val; chestTreasure[i].push_back(val);
			}
		}
		vector<int> res = bt(0, availKeys);
		if (!calculated) { cout << "Case #" << (t+1) << ": IMPOSSIBLE\n"; continue; }
		cout << "Case #" << (t+1) << ":";
		reverse(res.begin(), res.end());
		for (int i = 0; i < res.size(); i++) {
			cout << " " << (res[i]+1);
		}
		cout << "\n";
	}
	return 0;
}
