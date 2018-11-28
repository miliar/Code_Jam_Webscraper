#include <bits/stdc++.h>

using namespace std;


int main() {
	freopen("C:\\Users\\Omar Mohamed\\Downloads\\B-large.in", "r", stdin);
	freopen("C:\\Users\\Omar Mohamed\\ClionProjects\\Go\\output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int result = 0;
		string S;
		cin >> S;
		while (true) {
			bool found(true);
			for (int i = 0; i < S.size(); i++) {
				if (S[i] == '-') {
					found = false;
					break;
				}
			}
			if (found)
				break;

			if (S[0] == '-') {
				for (int i = 0; i < S.size() && S[i] == '-'; i++)
					S[i] = '+';
			} else {
				for (int i = 0; i < S.size() && S[i] == '+'; i++)
					S[i] = '-';
			}
			result++;
		}


		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}

/*
-+--++--+-
----++--+-		(1)
--++++--+-		(2)
++++++--+-		(3)
++++++--+-		(4)
--------+-		(5)
+++++++++-		(6)
----------		(7)
++++++++++		(8)


-+--++---

 */