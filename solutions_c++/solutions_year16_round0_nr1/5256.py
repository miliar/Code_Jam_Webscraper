#include <iostream>
using namespace std;
int main(void)
{
	int t, n;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n;
		cout << "Case #" << i << ": ";
		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		
		int cur = n;
		int appear[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		while (true)
		{
			int remain = cur;
			while (remain > 0)
			{
				appear[remain % 10] = 1;
				remain /= 10;
			}
			int sum = 0;
			for (int k = 0; k < 10; ++k)
			{
				sum += appear[k];
			}
			if (sum == 10)
			{
				cout << cur << endl;
				break;
			}
			cur += n;
		}

	}

	return 0;
}
