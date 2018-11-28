#include<iostream>
using namespace std;
int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int k = 1;
	while (t--)
	{
		cout << "Case #" << k << ": ";
		k++;
		long long n;
		cin >> n;
		if (n == 0)
		{
			cout << "INSOMNIA\n";
			continue;
		}
		int c[10] = { 0 };
		bool f = 1;
		long long num = n;
		while (f)
		{
			long long x = num;
			while (x)
			{
				c[x % 10]++;
				x /= 10;
			}
			f = 0;
			for (int i = 0; i < 10; i++)
				if (!c[i])
					f = 1;
			num += n;
		}
		cout << num - n << endl;
	}
	return 0;
}