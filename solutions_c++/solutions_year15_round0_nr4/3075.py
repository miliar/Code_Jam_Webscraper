#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main () {
	int t;
	freopen ("4.in", "r", stdin);
	freopen ("4.out", "w", stdout);
	scanf ("%d", &t);
	for (int tt = 0; tt < t; tt++) {
		int x, r, c;
		scanf ("%d%d%d", &x, &r, &c);
		int ans = 0;
		switch (x) {
			case (1) : {
				ans = 2;
				break;
			}
			case (2) : {
				if (r * c % 2 == 0)
					ans = 2;
				else
					ans = 1;
				break;
			}
			cout << "asd" << endl;
			case (3) : {
				if (r * c % 3 == 0) {
					if (c * r == 3)
						ans = 1;
					else
						ans = 2;
				} else {
					ans = 1;
				}
				break;
			}
			case (4) : {
				if (r * c % 4 != 0)
					ans = 1;
				else
					if (r * c < 12)
						ans = 1;
					else
						ans = 2;
				break;
			}
		}
		if (ans == 1)
			printf ("case #%d: RICHARD\n", tt + 1);
		else
			printf ("case #%d: GABRIEL\n", tt + 1);
	}
}

