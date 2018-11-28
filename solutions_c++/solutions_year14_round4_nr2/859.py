#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

long long solve() {
	int N;
	cin >> N;
	vector<int> v(N);
	for (int i = 0; i < N; ++i)
		cin >> v[i];
	long long res = 0;
	while (!v.empty()) {
		int ind = min_element(v.begin(), v.end()) - v.begin();
		int rind = v.size()-1 - ind;
		res += min(ind, rind);
		v.erase(v.begin() + ind);
	}
	return res;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
