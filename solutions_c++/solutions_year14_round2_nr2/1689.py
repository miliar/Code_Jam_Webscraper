#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long _int64;

int ABS(int x) { return x < 0 ? -x : x ; }

int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int cas, T;
	
	for (cas = scanf("%d", &T); cas <= T; cas++)
	{
		_int64 A, B, K;
		cin >> A >> B >> K;
		
		_int64 ans = 0;
		for (_int64 x = 0; x < A; x++) 
			for (_int64 y = 0; y < B; y++)
			{
				if ((x & y) < K) ans++;
			}
	
		
		printf("Case #%d: ", cas);

		cout << ans << endl;
	}
	return 0;
}
