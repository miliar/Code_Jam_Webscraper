# include <iostream>
# include <fstream>
# include <algorithm>
# include <cmath>
# include <cstdio>
# include <cstdlib>
# include <cstring>
# include <string>
# include <vector>
# include <stack>
# include <queue>
# include <map>

using namespace std;

int a, b, k;

int ans;

int main ()
{
	int t, te, i, j;
	cin >> t;
	for (te = 1; te <= t; te ++)
	{
		ans = 0;
		cin >> a >> b >> k;
		for (i = 0; i < a; i ++)
			for (j = 0; j < b; j ++)
				if ((i & j) < k) ans ++;
		cout << "Case #" << te << ": " << ans << endl;
	}

	return 0;
}

