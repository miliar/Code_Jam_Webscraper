#include <iostream>
#include <string>
#include <limits.h>
using namespace std;

#define N 16
#define J 50

int Prime(unsigned long long a)
{
	unsigned long i1, i2, i3, i4, i5, i6, i7, i8, bound;
	if (a == 0 || a == 1)
		return 0;
	if (a == 2 || a == 3 || a == 5 || a == 7 || a == 11 || a == 13 || a == 17 || a == 19 || a == 23 || a == 29)
		return 1;
	if (a % 2 == 0 || a % 3 == 0 || a % 5 == 0 || a % 7 == 0 || a % 11 == 0 || a % 13 == 0 || a % 17 == 0 || a % 19 == 0 || a % 23 == 0 || a % 29 == 0)
		return 0;

	bound = pow((double)a, 0.5);
	i1 = 31; i2 = 37; i3 = 41; i4 = 43; i5 = 47; i6 = 49; i7 = 53; i8 = 59;
	while (i8 <= bound && a%i1 && a%i2 && a%i3 && a%i4 && a%i5 && a%i6 && a%i7 && a%i8)
	{
		i1 += 30; i2 += 30; i3 += 30; i4 += 30; i5 += 30; i6 += 30; i7 += 30; i8 += 30;
	}
	if (i8 <= bound ||
		i1 <= bound && a % i1 == 0 ||
		i2 <= bound && a % i2 == 0 ||
		i3 <= bound && a % i3 == 0 ||
		i4 <= bound && a % i4 == 0 ||
		i5 <= bound && a % i5 == 0 ||
		i6 <= bound && a % i6 == 0 ||
		i7 <= bound && a % i7 == 0)
		return 0;
	return 1;
}

void main()
{
	cout << "Case #1:" << endl;
	int t, a, b;
	cin >> t >> a >> b;

	int count = 0;
	unsigned long long values[9];
	unsigned short start = strtoul("1000000000000001", nullptr, 2);
	for (unsigned short i = start; count < J; i++)
	{
		char buff[N + 1];
		_ultoa_s(i, buff, 2);

		if (buff[strlen(buff) - 1] == '0')
			continue;

		bool IsCoin = true;
		for (int j = 0; j < 9; j++)
		{
			values[j] = strtoull(buff, nullptr, j + 2);
			
			if (Prime(values[j]))
			{
				IsCoin = false;
				break;
			}
		}

		if (!IsCoin)
			continue;

		cout << buff;

		for (int j = 0; j < 9; j++)
		{
			for (unsigned long long k = 2; true; k++)
			{
				if (values[j] % k == 0)
				{
					cout << " " << k;
					break;
				}					
			}
		}
		cout << endl;
		count++;
	}
}