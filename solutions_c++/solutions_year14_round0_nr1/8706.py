#include <bits/stdc++.h>

using namespace std;
int main() {
	ios_base::sync_with_stdio(0);
	ofstream cout("test.out");
	ifstream cin("A-small-practice.in");
	int n, x[4], y[4], tmp;
	cin >> n;
	for (int j = 1; cin >> n; ++j) {
		cout << "Case #" << j << ": ";
		--n;
		for (int i = 0; i < n * 4; cin >> tmp, ++i)
			;
		for (int i = 0; i < 4; cin >> x[i++])
			;
		n = 3 - n;
		for (int i = 0; i < n * 4; cin >> tmp, ++i)
			;
		cin >> n;
		--n;
		for (int i = 0; i < n * 4; cin >> tmp, ++i)
			;
		for (int i = 0; i < 4; cin >> y[i++])
			;
		n = 3 - n;
		for (int i = 0; i < n * 4; cin >> tmp, ++i)
			;
		n = 0;
		for (int i = 0; i < 4; ++i)
			if (count(y, y + 4, x[i])) {
				if (n) {
					cout << "Bad magician!" << endl;
					goto r;
				} else
					tmp = x[i], n++;
			}
		if (n)
			cout << tmp << endl;
		else
			cout << "Volunteer cheated!" << endl;
		r: ;
	}

	return 0;
}
