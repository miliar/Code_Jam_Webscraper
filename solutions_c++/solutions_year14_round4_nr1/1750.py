#include <utility>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int num(vector<int> c, int x) {
	sort(c.begin(), c.end());
	int count = 0;
	for (int i = 0, j = c.size()-1; i <= j; j--) {
		count++;
		if (c[i] + c[j] <= x) {
			i++;
		}
	}
	return count;
}

int main() {
	int T;
	int N, X;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> X;
		cout << "Case #" << i+1 << ": ";
		vector<int> c(N);
		for (int j = 0; j < N; j++) {
			cin >> c[j];
		}
		cout << num(c, X) << endl;
	}
	return 0;
}