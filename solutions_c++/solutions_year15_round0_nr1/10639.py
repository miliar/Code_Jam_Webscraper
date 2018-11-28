#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("b.in", "w", stdout);
	int t;
	cin >> t;
	int j = 1;
	while (t--)
	{
		int n;
		string a;
		cin >> n >> a;
		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= n; i++)
		{
			if (a[i] == '0')
				continue;
			if (i > sum)
			{
				ans += i-sum;
				sum += i-sum;
			}
			sum += a[i] - 48;
		}
		cout << "Case #" << j << ": " << ans << endl;
		j++;
	}

	
	return 0;
}