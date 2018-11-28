#include <iostream>

using namespace std;

const int Max = 5555;
int n;
int num[Max];

void calc(int number)
{
	for (int i = 0; i < Max; i++)
		num[i] = 0;
	cin >> n;
	for (int i = 1; i <= 2 * n - 1; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			int c;
			cin >> c;
			num[c]++;
		}
	}
	cout << "Case #" << number << ":";
	int pr = 0;
	for (int i = 0; i < Max; i++)
	{
		if (num[i] % 2 == 1)
		{
			cout << ' ' << i;
			pr++;
		}
	}
	cout << endl;
	if (pr != n)
	{
		while (true)
		{
		}
	}
	return;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out-4.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		calc(i);
	}
	return 0;
}