#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-Large.txt", "w", stdout);

	int t;
	
	cin >> t;

	for (int l = 0; l < t; l++) {
	int x;
	int y;
	int k;

	cin >> x >> y >> k;

	int c = 0;

	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			int p = i & j;
			if (p < k && p >= 0) {
				c++;
			}
		}
	}

	cout << "Case #" << l + 1 << ": " << c << endl;
	}

	return 0;
}
