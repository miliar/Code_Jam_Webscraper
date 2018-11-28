#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

#define IN_FILE "A-small-attempt0.in"
#define OUT_FILE "output.txt"

using namespace std;

int main(int argc, char const *argv[]) { 

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		
		int r;
		cin >> r; --r;
		
		vector<int> row, row2, ans;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int c;
				cin >> c;
				if (r == i)
					row.push_back(c);
			}

		cin >> r; --r;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int c;
				cin >> c;
				if (r == i)
					row2.push_back(c);
			}

		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				if (row[i] == row2[j])
					ans.push_back(row[i]);
			}

		cout << "Case #" << t + 1 << ": ";
		if (ans.size() == 0) {
			 cout << "Volunteer cheated!" << endl;
		} else if (ans.size() == 1) {
			cout << ans[0] << endl;
		} else {
			cout << "Bad magician!" << endl;
		}

	}

	return 0;
}