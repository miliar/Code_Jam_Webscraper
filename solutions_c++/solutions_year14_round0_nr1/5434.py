# include <string>
# include <fstream>
# include <algorithm>
# include <set>
# include <map>
# include <vector>
using namespace std;


int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;

	for (int test = 0; test < tests; test++) {
		vector<int> f(17, 0);
		int row1;
		cin >> row1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int q;
				cin >> q;
				if (i == row1 - 1)
					f[q]++;
			}
		}
		int row2;
		cin >> row2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int q;
				cin >> q;
				if (i == row2 - 1)
					f[q]++;
			}
		}

		int ans, count = 0;
		for (int i = 0; i <= 16; i++)
		if (f[i] == 2) {
			count++;
			ans = i;
		}
		
		cout << "Case #" << test + 1 << ": ";

		if (count == 0)
			cout << "Volunteer cheated!";
		else if (count == 1)
			cout << ans;
		else
			cout << "Bad magician!";

		cout << endl;

	}

	return 0;
}