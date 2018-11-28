#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t;
string s;

int comp(int x, bool y = true) {
	if (x == -1)
		return 0;

	if ((s[x] == '+')^y)
		return comp(x-1, !y)+1;
	else
		return comp(x-1, y);
}

int main() {
	ifstream cin("input.txt");

	cin >> t;

	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i+1 << ": ";

		cin >> s;
		cout << comp(s.length()-1) << "\n";
	}
}