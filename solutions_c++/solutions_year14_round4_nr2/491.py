#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

int solve() {
	int N;
	cin >> N;
	assert(N >= 1 && N <= 1000);
	vector<int> a(N);
	for (int i = 0; i < N; i++) {
		cin >> a[i];
		assert(a[i] >= 1 && a[i] <= 1000000000);
	}
	vector<int> b = a;
	sort(b.begin(), b.end());
	int ret = 0;
	for (int i = 0; i < N; i++) {
		vector<int>::iterator pos = find(a.begin(), a.end(), b[i]);
		assert(pos != a.end());
		//cerr << "  distance to begin: " << (pos - a.begin()) << ", distance to end: " << (a.end() - pos - 1) << endl;
		int links = pos - a.begin();
		int rechts = a.end() - pos - 1;
		assert(links >= 0 && links < N - i);
		assert(rechts >= 0 && rechts < N - i);
		ret += min(links, rechts);
		a.erase(pos);
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": " << solve() << endl;
	}
	return 0;
}
