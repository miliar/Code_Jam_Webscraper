#include <algorithm>
#include <vector>
#include <string>
#include <ctime>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

bool tab[20][20];

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int tt = 0; tt < T; ++tt)
	{
		int n, m, N;
		cin >> n >> m >> N;
		int nm = n * m;
		int ans = 1e9;
		for (int msk = (1 << nm)-1; msk >= 0; --msk)
		{
			int qq = 0;
			for (int i = 0; i < nm; ++i)
				qq += (msk & (1 << i)) ? 1 : 0;
			if (qq != N)
				continue;
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < m; ++j)
					tab[i][j] = msk & (1 << (m*i + j));
			int q = 0;
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < m; ++j)
				{
					if (i)
					q += tab[i][j] & tab[i - 1][j];
					if (j)
					q += tab[i][j] & tab[i][j - 1];
				}
					
			ans = min(ans, q);
		}
		printf("Case #%d: %lld\n", tt + 1, ans);
	}
	return 0;
}

/*

*/