#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int k = 0; k < t; k++) {
		int S;
		cin >> S;

		string s;
		cin >> s;

		int a[S + 1];
		for (int i = 0; i < S + 1; i++) {
			a[i] = s[i] - '0';
		}

		int ppl = 0;
		int extra = 0;

		for (int i = 0; i < S + 1; i++) {
			if (ppl < i) {
				int diff = i - ppl;
				extra += diff;
				ppl += diff;
			}
			ppl += a[i];
		}
		cout << "Case #" << k + 1 << ": ";
		cout << extra << endl;
	}

	return 0;
}
