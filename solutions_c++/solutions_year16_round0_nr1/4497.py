#include <iostream>

using namespace std;

long long n;
bool mask[11];

long long calc(long long v)
{
	for (int i = 0; i < 11; i++)
		mask[i] = false;
	int num = 10;
	for (long long i = 1; i <= 1000000; i++)
	{
		long long V = v * i;
		while (V > 0)
		{
			long long u = V % 10;
			if (!mask[u])
			{
				mask[u] = true;
				num--;
			}
			V /= 10;
		}
		if (num == 0)
			return (v * i);
	}
	return -1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out-large.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		cout << "Case #" << i << ": ";
		long long ans = calc(n);
		if (ans == -1)
			cout << "INSOMNIA" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}