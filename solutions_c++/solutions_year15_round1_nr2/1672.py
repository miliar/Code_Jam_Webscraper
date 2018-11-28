#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <algorithm>
using namespace std;

int data[10005];

int ans[1000000];
int gcd(int a, int b)
{
	return (b == 0) ? a : gcd(b, a%b);
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T, index=1;
	cin >> T;
	while (T--)
	{
		cout << "Case #" << index++ << ": ";
		int b, n;
		cin >> b >> n;
		for (int i = 1; i <= b; ++i)cin >> data[i];
		if (n <= b)cout << n << endl;
		else if (b == 1)cout << 1 << endl;
		else
		{
			int lcm = data[1];
			for (int i = 2; i <= b; ++i)
			{
				lcm = (lcm*data[i]) / gcd(lcm, data[i]);
			}
			map<int, int> imap;
			for (int i = 1; i <= b; ++i)imap[i] = 1, ans[i] = i;
			for (int i = b + 1; i <= n; ++i)
			{
				int mint = 100000000;
				int minindex = -1;
				for (int j = 1; j <= b; ++j)
				{
					int t = data[j] * imap[j];
					if (t < mint)
					{
						mint = t;
						minindex = j;
					}
				}
				ans[i] = minindex;
				imap[minindex]++;
				if (i == n)
				{
					cout << ans[i] << endl;
					break;
				}
				else if (mint == lcm)
				{
					cout << ans[((n - 1) % (i - 1) + 1)] << endl;
					break;
				}
			}
			//cout << ans[((n - 1) % lcm) + 1] << endl;
		}
	}
	return 0;
}