#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
	int t, no, r[17], r1, r2, c, ans;

	cin >> t;
	for (int cc = 1; cc <= t; cc++) {
		printf("Case #%d: ", cc);

		memset(r, 0, sizeof r);
		cin >> r1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				cin >> no;
				if (i + 1 == r1)
					r[no]++;
			}
		
		cin >> r2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				cin >> no;
				if (i + 1 == r2)
					r[no]++;
			}

		c = 0;
		for (int i = 1; i <= 16; i++)
			if (r[i] == 2)
				c++, ans = i;
		if (c == 1)
			printf("%d\n", ans);
		else if (c > 1)
			puts("Bad magician!");
		else
			puts("Volunteer cheated!");
	}

	return 0;
}