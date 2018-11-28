#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> scan() {
	vector<int> ret;
	int r;
	cin >> r;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) {
			int t;
			cin >> t;
			if (i == r - 1)
				ret.push_back(t);
		}
	return ret;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		vector<int> s1 = scan(), s2 = scan(), s(4);
		sort(s1.begin(), s1.end());
		sort(s2.begin(), s2.end());
		auto it = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), s.begin());
		cout << "Case #" << t << ": ";
		int k = it - s.begin();
		if (k == 1)
			cout << s[0];
		else if (k > 1) 
			cout << "Bad magician!";
		else 
			cout << "Volunteer cheated!";
		cout << endl;
	}
}
