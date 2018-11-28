#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		int n;
		cin >> n;
		map<int, int> count;
		for (int i = 0; i < 2 * n - 1; i++) {
			for (int j = 0; j < n; j++) {
				int num;
				cin >> num;
				count[num]++;
			}
		}

		vector<int> sol;
		for (map<int, int>::iterator it = count.begin(); it != count.end(); ++it)
			if (count[it->first] & 1)
				sol.push_back(it->first);
		sort(sol.begin(), sol.end());

		cout << "Case #" << caseCounter << ":";
		for (int i = 0; i < sol.size(); i++)
			cout << " " << sol[i];
		cout << endl;
	}

	return 0;
}
