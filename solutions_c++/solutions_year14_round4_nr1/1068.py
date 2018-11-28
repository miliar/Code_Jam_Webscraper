#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 0; tc < t; tc++)
	{
		int n, s;
		cin >> n >> s;
		vector <int> arr(n);
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		sort(arr.rbegin(), arr.rend());
		int r = n - 1;
		int ans = 0;
		for (int i = 0; i <= r; i++)
		{
			if (arr[r] + arr[i] <= s)
				r--;
			ans++;
		}
		printf("Case #%d: %d\n", tc + 1, ans);
	}
}