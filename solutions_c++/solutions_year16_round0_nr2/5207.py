#include <iostream>
#include <set>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

const int inf = 1e9;

int solve(vector <int> &v) {
	int r = v.size() - 1;
	int cnt = 0;
	while (r >= 0) {
		if (v[r] == 0)
		{
			int l = 0;
			while (l < r && v[l] == 1) l++;
			if (l != 0) {
				cnt++;
				for (int i = 0; i < l; i++)
					v[i] = 0;
			}

			cnt++;

//			[0,4]
//			 01234
			for (int i = 0; i <= r / 2; i++) {
				int j = r - i;
				swap(v[i], v[j]);
				v[i] = 1 - v[i];
				if (i == j) continue;
				v[j] = 1 - v[j];
			}
		}
		while (r >= 0 && v[r] == 1) r--;

	}
	return cnt;
}

void output(int caseNum, long long res) {

	if (res == -1) {
		cout << "Case " << "#" << caseNum << ": " << "INSOMNIA" << endl;
	} else
	cout << "Case " << "#" << caseNum << ": " << res << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		vector <int> v;
		for (int i = 0; i < s.size(); i++)
			if (s[i] == '+') v.push_back(1);
			else
				v.push_back(0);

		output(t, solve(v));
	}

}
