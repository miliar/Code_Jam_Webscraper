#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void solve(int case_no) {
	int n, num, ans;
	vector<int> a, sa;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		a.push_back(num);
		sa.push_back(num);
	}

	sort(sa.begin(), sa.end());

	ans = 0;
	for (int i = 0; a.size() > 1; i++) {
		int min_a = sa[i];
		for (vector<int>::iterator it = a.begin(); it != a.end(); it++)
			if (*it == min_a) {
				ans += min((int) (it - a.begin()), (int) (a.end() - it) - 1);
				a.erase(it);
				break;
			}
	}

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