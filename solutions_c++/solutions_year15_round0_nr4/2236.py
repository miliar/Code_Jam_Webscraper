#include <bits/stdc++.h>

using namespace std;

void win(int t) {
	printf("Case #%d: RICHARD\n", t);
}

void lose(int t) {
	printf("Case #%d: GABRIEL\n", t);
}

int main() {
	int t;
	cin >> t;
	
	for (int test = 1; test <= t; test++) {
		int x, r, c;
		cin >> x >> r >> c;

		if ((r * c) % x != 0) {
			win(test);
			continue;
		}

		if (r * c < x) {
			win(test);
			continue;
		}

		if (x == 1 || x == 2) {
			lose(test);
		} else if (x == 3) {
			if (min(r, c) == 1) {
				win(test);
			} else {
				lose(test);
			}
		} else if (x == 4) {
			if (min(r, c) <= 2) {
				win(test);
			} else {
				lose(test);
			}
		}
	}
}

//3
//1 9 3

//1 5 4 3     1 6 3 3
//1 3 2 4 3   1 3 3 3 3