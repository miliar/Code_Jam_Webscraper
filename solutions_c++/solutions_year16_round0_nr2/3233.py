#include <bits/stdc++.h>

using namespace std;

int T;
string s;

void load () {
	cin >> s;
}

int solve () {
	int res = 0;
	int add;

	for (int i = 0; i < (int) s.size (); i++) {
		if (s[i] == '-') {
			add = 0;
			if (i) add = 1;

			int pos = i;
			while (pos < (int) s.size () && s[pos] == '-') {
				pos++;
			}
			res += add + 1;
			i = pos - 1;
		}
	}

	return res;		
}

int main () {                         
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		cout << "Case #" << tc << ": " << solve () << "\n";
	}

	return 0;
}