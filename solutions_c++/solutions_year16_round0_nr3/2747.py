#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, j, k, l;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> n >> j;
		cout << "Case #" << i << ":" << endl;
		for(k = (1 << n - 1) + 1; k < 1 << n; k += 2)
		{
			int base, divisors[11];
			for(base = 2; base <= 10; base++)
			{
				bool found = false;
				int temp = k;
				unsigned long long k_base = 0;
				while(temp != 0)
				{
					k_base = k_base * base + (temp & 1);
					temp >>= 1;
				}
				divisors[1] = k_base;
				for(int l2 = 3; l2 <= floor(sqrt(k_base)); l2 += 2)
					if(k_base % l2 == 0)
					{
						divisors[base] = l2;
						found = true;
						break;
					}
				if(!found)
					break;
			}
			if(base == 11)
			{
				int temp = k;
				while(temp != 0)
				{
					cout << (temp & 1);
					temp >>= 1;
				}
				for(int base = 2; base <= 10; base++)
					cout << " " << divisors[base];
				cout << endl;
				j--;
				if(j == 0)
					break;
			}
		}
	}
	return 0;
}

