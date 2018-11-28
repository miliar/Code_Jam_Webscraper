#include <iostream>
#include <vector>

using namespace std;

void solve(int case_no) {
	int n, x, si, ans;
	vector<int> s;

	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		cin >> si;
		s.push_back(si);
	}

	sort(s.begin(), s.end());

	ans = 0;
	for (int i = 0, j = n - 1; j >= i; j--, ans++)
		if (i != j && s[i] + s[j] <= x)
			i++;

	cout << "Case #" << case_no << ": " << ans << endl;
}

int main(int argc, char* argv[]) {
	int t;

	ios::sync_with_stdio(0);

	cin >> t;
	for (int case_no = 1; case_no <= t; case_no++)
		solve(case_no);

	return 0;
}