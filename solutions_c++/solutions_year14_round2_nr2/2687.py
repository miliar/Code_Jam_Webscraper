#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		unsigned int a, b, k;
		int ans = 0;
		cin >> a >> b >> k;
		for (int m = 0; m < a; m++)
		{
			for (int n = 0; n < b; n++)
			{
				int x = m&n;
				if (x < k)
				{
					ans++;
				}
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}