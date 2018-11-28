#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;


int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt)
	{
		int x, r, c;
		cin >> x >> r >> c;
		bool ans = (x == 1 || x == 2 && (r*c) % 2 == 0 ||
			x == 3 && abs(r - 3) + abs(c - 3) <= 1 ||
			x == 4 && abs(r - 4) + abs(c - 4) <= 1);

		printf("Case #%d: %s\n", tt, ans ? "GABRIEL" : "RICHARD");
	}

	return 0;
}