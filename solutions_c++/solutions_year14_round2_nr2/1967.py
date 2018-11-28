#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <string>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T = 0, A, B, K;
	long long ans = 0;
	cin >> T;

	for (int q = 0; q < T; q++)
	{
		ans = 0;
		cin >> A >> B >> K;
		for (int i = 0; i < A; i++)
			for (int j = 0; j < B; j++)
			{
				int temp = i & j;
				if ( temp < K )
					ans ++;
			}

		cout << "Case #" << q + 1 << ": " << ans << endl;
	}
	return 0;
}
