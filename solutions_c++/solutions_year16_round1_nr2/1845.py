#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int T;
	int x, n;
	int arr[2600];

	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> n;
		memset(arr, 0, sizeof(arr));

		for (int j = 0; j < (2 * n - 1); ++j) {
			for (int k = 0; k < n; ++k) {
				cin >> x;
				++arr[x];
			}
		}

		bool flag = false;
		cout << "Case #" << i << ": ";
		for (int j = 1; j <= 2500; ++j) {

			if (arr[j] % 2 == 1) {
				if (flag) {
					cout << " ";
				}
				cout << j;
				flag = true;
			}
		}
		cout << "\n";

	}
	
	return 0;
}