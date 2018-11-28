#include <bits/stdc++.h>
#define LOG(x) // cout << #x << " is " << x << endl;
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int cases;
	cin >> cases;

	int n;

	for (int i = 0; i < cases; i++) {
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i+1 << ": ";
			cout << "INSOMNIA" << '\n';
			continue;
		}
		int all = 0b1111111111;
		int seen = 0;
		int num = 1;
		int last = n;
		while (seen != all) {
			int curr = num * n;
			last = curr;
			while (curr >= 1) {
				int digit = curr % 10;
				seen = seen | 1 << digit;
				curr -= digit;
				curr /= 10;
			}
			num++;
		}

		cout << "Case #" << i+1 << ": " << last << '\n';
	}


	return 0;
}