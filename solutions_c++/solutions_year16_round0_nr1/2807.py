#include<bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);

//	freopen("prelim-a.in", "r", stdin);
//	freopen("prelim-a.res", "w", stdout);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		
		int k;
		cin >> k;

		int arr[10] {0};

		cout << "Case #" << i << ": ";

		if (k == 0) {
			cout << "INSOMNIA";
		} else {
			for (int j = 1; true; j++) {
				int num = k * j;
				
				while (num != 0) {
					int digit = num % 10;
					if (arr[digit] == 0) { arr[digit]++; }
					num /= 10;
				}

				int count = 0;
				for (int m = 0; m < 10; m++) {
					count += arr[m];
				}
				if (count == 10) { cout << (k * j); break; }
			}
		}

		cout << endl;
	}
}
