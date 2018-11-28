#include <iostream>

using namespace std;

int main()
{
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int a, b, k, ans;
		cin >> a >> b >> k;
		ans = 0;
		for (int x = 0; x < a; x++)
			for (int y = 0; y < b; y++)
				if ((x & y) < k)
					ans++;
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}