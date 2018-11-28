#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility>
#include <iterator>
#include <algorithm>
using namespace std;

vector<int> rankfile(vector<vector<int> > v, int size) {
	//if (v.empty() || v[0].empty()) return vector<int>();
	int n = v.size();
	int m = v[0].size();
	unordered_map<int, pair<int, int> > map;
	for(int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map.find(v[i][j]) == map.end()) {
				map[v[i][j]] = make_pair(1, i);
			} else {
				map[v[i][j]].first++;
				//int temp = map[v[i][j]].second;
				//map[v[i][j]].second = temp ^ i;
			}
		}
	}

	unordered_map<int, pair<int, int> >::iterator it = map.begin();
	vector<int> result;
	
	while(it != map.end()) {
		if(((it->second).first) % 2 == 1) {
			result.push_back(it -> first); 
		}
		it++;
	}
	
	sort(result.begin(), result.end());
	return result;

}

int main() {
	int t;
	int n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		vector<vector<int> > v;

		for (int k = 0; k < (2 * n - 1); k++) {
			vector<int> path(n, 0);
			int temp;
			for (int j = 0; j < n; j++) {
				cin >> temp;
				path[j] = temp;
			}
			v.push_back(path);

		}
		
		vector<int> result = rankfile(v, n);
		cout << "Case #" << i << ":";
		
		for (int j = 0; j < n; j++) {
			cout << " " << result[j];
		}
		
		cout << "\n";
		
	}
}