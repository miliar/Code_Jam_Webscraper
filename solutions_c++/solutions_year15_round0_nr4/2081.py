#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;

int main() {
	freopen("/mnt/S/Code/in.txt", "rt", stdin);
	freopen("/mnt/S/Code/out.txt", "wt", stdout);

	int n, x, r, c;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		bool g = 0; //g true print gabriel
		cin >> x >> r >> c;
		if (x > (c * r) || (x > r && x > c) || (r * c) % x != 0)g = 0;

		else if (x == 1)g = 1;

		else if (x == 2)g = 1;

		else if (x == 3)
		{
			if (c * r == 3)g = 0;
			else g = 1;
		}

		else if (x == 4) {
			if (c * r == 4)g = 0;
			else if (c * r == 8)g = 0;
			else g = 1;
		}
		cout << "Case #" << i + 1 << ": ";
		if (g)cout << "GABRIEL" << endl;
		else cout << "RICHARD" << endl;
	}
	return 0;
}
