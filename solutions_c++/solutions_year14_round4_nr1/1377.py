#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

int N[10005];
int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int cas, T;
	
	for (cas = scanf("%d", &T); cas <= T; cas++)
	{
		int n, m;
		cin >> n >> m;
		
		for (int i = 1; i <= n; i++) cin >> N[i];
		
		sort(N + 1, N + n + 1);
		
		int l = 1, r = n;
		
		int ans = 0;
		for (int i = 1; i <= r; i++)
		{
			while (N[i] + N[r] > m && r > i) r--; 
			if (r <= i) break;
			ans ++;
			r--;
		}
		
		printf("Case #%d: ", cas);
		cout << n - ans << endl;
	}
	
	return 0;
}
