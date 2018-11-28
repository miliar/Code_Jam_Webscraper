#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;

int grid1[4][4], grid2[4][4];

int main()
{
	int t;
	cin >> t;

	for (int test = 0; test < t; ++test)
	{
		int a, b;

		cin >> a;
		--a;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> grid1[i][j];

		cin >> b;
		--b;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> grid2[i][j];

		int ans = -1;
		for (int fv = 0; fv < 4; ++fv)
			for (int sv = 0; sv < 4; ++sv)
				if (grid1[a][fv] == grid2[b][sv])
					if (ans == -1)
						ans = grid1[a][fv];
					else
						ans = 100;

		cout << "Case #" << test + 1 << ": ";
		if (ans == -1)
			cout << "Volunteer cheated!";
		else if (ans == 100)
			cout << "Bad magician!";
		else
			cout << ans;
		cout << "\n";
	}

	return 0;
}
