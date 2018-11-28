#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <sstream>
#include <tuple>
#include <cstring>

using namespace std;


inline int solve(vector<int>& a, int s) {
	sort(a.begin(), a.end());
	int ans = a.size();
	for (int i = 0, j = a.size() - 1; i < a.size(); i++) {
		while (i < j && a[i] + a[j] > s) j--;
		if (i < j && a[i] + a[j] <= s) ans--, j--;
	}

	return ans;
}

int main() {
	ifstream cin("test.in");
	ofstream cout("test.out");
	int testCount;
	cin >> testCount;
	for (int t = 1; t <= testCount; t++) {
	
		int n, s;
		cin >> n >> s;
		vector<int> a(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];

		sort(a.begin(), a.end());

		cout << "Case #" << t << ": " << solve(a, s) << "\n";
	}
	return 0;
}