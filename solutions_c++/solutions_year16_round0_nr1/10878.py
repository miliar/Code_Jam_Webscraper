#include <bits/stdc++.h>

using namespace std;

int main () {

	int t, n, c = 0;
	cin >> t;
	while (t--) {
		c++;
		cin >> n;
		int res = 0;

		if (n == 0) {
			res = -1;
		} else {
			set <int> p;
			for (int i = 0; i <= 9; i++)
				p.insert(i);
			int x;
			for (int k = 1; !p.empty(); k++) {
				x = k * n;
				int temp = x;
				while (temp) {
					if (p.count(temp % 10) > 0) {
						p.erase(temp % 10);
					}
					temp /= 10;
				}
			}
			res = x;
		}

		
		printf("Case #%d: ", c);

		if (res == -1)
			printf("INSOMNIA");
		else
			printf("%d", res);

		if (t > 0)
			printf("\n");
	
	}

	return 0;
}