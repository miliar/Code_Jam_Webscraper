#include<bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	freopen("prelim-b.in", "r", stdin);
	freopen("prelim-b.res", "w", stdout);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		string pancake;
		cin >> pancake;

		cout << "Case #" << i << ": ";
		int count = 0;
		for (int j = 0; j < pancake.size() - 1; j++) {
			char curr = pancake[j];
			char next = pancake[j + 1];

			if (curr != next) {
				count++;
			}
		}
		if (pancake[pancake.size() - 1] != '+') {
			count++;
		}

		cout << count << endl;
	}
}
