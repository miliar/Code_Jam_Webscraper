#include <iostream>
#include <set>

using namespace std;

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i) {
		int c1;
		
		cin >> c1;
		cout << "Case #" << i << ": ";
		set<int> l1;
		int res = -1;

		for (int j = 1; j <= 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				int t;
				cin >> t;
				if (j == c1) l1.insert(t);
			}
		}

		cin >> c1;
		for (int j = 1; j <= 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				int t;
				cin >> t;
				if (j == c1) {
					if (l1.count(t) > 0) {
						if (res > 0) {
							cout << "Bad magician!" << endl;
							res = -2;
						}
						else if (res == -1) {
							res = t;
						}
					}
				}
			}
		}
		
		if (res == -1) {
			cout << "Volunteer cheated!" << endl;
		}
		else if (res > 0) {
			cout << res << endl;
		}

	}
	return 0;	
}
 

