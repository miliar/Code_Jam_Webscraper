#include <stdio.h>
#include <set>

using namespace std;

int t;

int main () {
	scanf ("%d", &t);
	for (int i = 0; i < t; i ++) {
		set<int> myset;
		int cnt = 1, n, n2;
		scanf ("%d", &n);
		if (n == 0) {
			printf ("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}

		n2 = n;
		while (n2 > 0) {
			myset.insert(n2 % 10);
			n2 /= 10;
		}
		while (myset.size() < 10) {
			cnt ++;
			n2 = n * cnt;
			while (n2 > 0) {
				myset.insert(n2 % 10);
				n2 /= 10;
			}			
		}

		printf ("Case #%d: %d\n", i + 1, n * cnt);
	}

	return 0;
}

