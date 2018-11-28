#include <algorithm>
#include <iostream>
using namespace std;

void swap(bool* row, int k) {
	reverse(row, row+k+1);
	for (int i = 0; i <= k; i++)
		row[i] = 1-row[i];
}

int solve(string x) {
	bool row[150];
	int N = x.size();
	for (int i = 0; i < N; i++)
		row[i] = x[i] == '+';
	int sol = 0;
	
	for (int i = N-1; i >= 0; i--) {
		if (row[i]) continue;
		if (row[0]) {
			int i = 0; 
			while (row[i]) i++;
			i--;
			swap(row, i);
			sol++;
		}
		sol++;
		swap(row, i);
	}
	return sol;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string x; cin >> x;
		cout << "Case #" << t << ": " << solve(x) << endl;
	}
}

