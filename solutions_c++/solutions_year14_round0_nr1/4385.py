#include <iostream>
#include <vector>
#include <map>

using namespace std;

int a1[5], a2[5], numCase=1;

int main() {
	int T, r1, r2, i, j, dc;
	cin >> T;
	while (T--) {
		cin >> r1;
		for (i = 1; i <= 4; ++i)
		for (j = 1; j <= 4; ++j) {
			if (i == r1)
				cin >> a1[j];
			else
				cin >> dc;
		}
		cin >> r2;
		for (i = 1; i <= 4; ++i)
		for (j = 1; j <= 4; ++j) {
			if (i == r2)
				cin >> a2[j];
			else
				cin >> dc;
		}
		map<int, int> freq;
		freq.clear();
		for (i = 1; i <= 4; ++i) {
			freq[a1[i]]++;
			freq[a2[i]]++;;
		}
		int n2 = 0, num = 0;
		for (auto p : freq) {
			if (p.second > 1) {
				n2++;
				num = p.first;
			}
		}
		cout << "Case #" << numCase++ << ": ";
		if (n2 == 1)
			cout << num << endl;
		else if (n2 > 1)
			cout << "Bad magician!\n";
		else
			cout << "Volunteer cheated!\n";			
	}
	return 0;
}