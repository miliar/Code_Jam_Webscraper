#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	freopen("problemA.in", "r", stdin);
	freopen("problemA.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		vector<int> row[2];
		for (int k = 0; k < 2; k++) {
			int reqRow;
			cin >> reqRow;
			cin.ignore(32, '\n');
			for (int j = 0; j < 4; j++) if (j == reqRow - 1) {
				for (int l = 0; l < 4; l++) {
					int t;
					cin >> t;
					row[k].push_back(t);
				}
				cin.ignore(32, '\n');
			}
			else cin.ignore(32, '\n');
		}

		sort(row[0].begin(), row[0].end());
		sort(row[1].begin(), row[1].end());

		vector<int> result(4);
		vector<int>::iterator it = set_intersection(row[0].begin(), row[0].end(), row[1].begin(), row[1].end(), result.begin());
		int intersections = distance(result.begin(), it);
		if (intersections == 0) {
			cout << "Case #" << i + 1 << ": Volunteer cheated!\n";
		} else if (intersections == 1) {
			cout << "Case #" << i + 1 << ": " << result[0] << "\n";
		} else {
			cout << "Case #" << i + 1 << ": Bad magician!\n";
		}
	}

	cout.flush();
	fclose(stdin);
	fclose(stdout);
	return 0;
}
