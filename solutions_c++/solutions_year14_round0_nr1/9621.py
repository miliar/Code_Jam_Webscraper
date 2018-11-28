#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t) {
		int ans1, ans2;
		int n = 4;
		int a[5], b[5];
		cin >> ans1;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				int x;
				cin >> x;
				if (i == ans1) a[j] = x;
			}
		cin >> ans2;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				int x;
				cin >> x;
				if (i == ans2) b[j] = x;
			}
		int count = 0;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (a[i] == b[j]) ++count;
		cout << "Case #" << t << ": ";
		if (!count) cout << "Volunteer cheated!" << endl;
		else if (count == 1) {
			for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (a[i] == b[j]) count = a[i];
			cout << count << endl;
		}
		else if (count > 1) cout << "Bad magician!" << endl;
	}
	return 0;
}