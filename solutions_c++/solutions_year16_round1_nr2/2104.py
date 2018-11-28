#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void doCase() {
	int N;
	cin >> N;
	
	int grid[105][55];
	for (int i=0; i<2*N-1; i++) {
		for (int j=0; j<N; j++) {
			cin >> grid[i][j];
		}
	}
	
	vector<int> ans;
	for (int i=0; i<N; i++) {
		int smallest = 2501;
		int a, b;
		
		int count[2505];
		for (int j=0; j<2505; j++) count[j] = 0;
		for (int j=0; j<2*N-1; j++) {
			if (grid[j][i] == 0) continue;
			if (grid[j][i] < smallest) {
				smallest = grid[j][i];
				a = j;
				b = -1;
			}
			else if (grid[j][i] == smallest) {
				b = j;
			}
			count[grid[j][i]]++;
		}
		
		if (b == -1) {
			ans.push_back(grid[a][i]);
			for (int j=0; j<N-i; j++) count[grid[a][i+j]]--;
			for (int j=1; j<2505; j++) {
				if (count[j] > 0) ans.push_back(j);
			}
			sort (ans.begin(), ans.end());
			for (int j=0; j<ans.size(); j++) cout << " " << ans[j];
			cout << endl;
			return;
		}
		
		for (int j=0; j<N-i; j++) {
			count[grid[a][i+j]]--;
			count[grid[b][i+j]]--;
			grid[a][i+j] = 0;
			grid[b][i+j] = 0;
		}
		for (int j=1; j<2505; j++) {
			if (count[j] < 0) {
				ans.push_back(j);
				break;
			}
		}
	}
	
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		cout << "Case #" << i+1 << ":";
		doCase();
	}
	return 0;
}