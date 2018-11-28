#include <cstdio>
#include <algorithm>

using namespace std;

int c[10];

inline void solve () {
	int n;
	scanf ("%d", &n);

	if (n == 0) {
		printf ("INSOMNIA\n");

		return ;
	}

	for (int i = 0;i < 10;i ++) {
		c[i] = 0;
	}

	int x = n;
	while (true) {
		int y = x;
		while (y > 0) {
			c[y%10] = 1;
			y /= 10;
		}

		for (int i = 0;i < 10;i ++) {
			if (c[i] == 0) {
				goto f;
			}
		}
		break;
		f:;

		x += n;
	}
	printf ("%d\n", x);
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		printf ("Case #%d: ", i);
		solve ();
	}
}