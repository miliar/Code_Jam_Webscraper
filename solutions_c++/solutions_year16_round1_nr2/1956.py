#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<int> find_lost(vector<vector<int>>& grid) {
	int a[2501] = { 0 };
	for (int i = 0; i < grid.size(); i++) {
		for (int j = 0; j < grid[0].size(); j++) {
			++a[grid[i][j]];
		}
	}
	vector<int> result;
	for (int i = 0; i < 2501; i++) {
		if (a[i] % 2 != 0) {
			result.push_back(i);
		}
	}
	sort(result.begin(), result.end());
	return result;
}

int main() {
	string s;
	getline(cin, s);
	int t = stoi(s);
	for (int i = 1; i <= t; i++) {
		int num;
		cin >> num;
		vector<vector<int>> grid(2 * num - 1, vector<int>(num));
		for (int j = 0; j < 2 * num - 1; j++) {
			for (int k = 0; k < num; k++) {
				cin >> grid[j][k];
			}
		}
		vector<int> result = find_lost(grid);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < result.size(); j++) {
			cout << result[j] << " ";
		}
		cout << endl;
	}
}
