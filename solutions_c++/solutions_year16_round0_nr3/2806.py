#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cmath>

using namespace std;

#define LL long long
#define size 16
#define pow2size 16384

void parseInt(int LL num, bool ans[size])
{
	int digit, i;
	//bool ans[size];

	for (i = size - 2; i > 0; i--)
	{
		digit = num % 2;
		ans[i] = digit;
		num = (num - digit) / 2;
	}

	//return ans;
}

LL check(bool data[size], int base)
{
	int i;
	LL num = 0, pow = 1;

	// interpreting number in our base
	for (i = size-1; i >= 0; i--)
	{
		num += data[i]*pow;
		pow *= base;
	}

	// cheking for divisors
	LL SQRT = sqrt(num);
	
	if (num % 2 == 0) return 2;

	for (i = 3; i <= SQRT; i+=2)
		if (num%i == 0)
			return i;
	
	// prime in our base
	return 0;
}

int main()
{
	int T, N, J;
	int j, counter = 0;
	long long i, ans[9] = { 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	bool data[size], jamcoin;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	cin >> N >> J;
	cout << "Case #1: " << endl;

	for (i = 0; i < pow2size; i++)
	{
		if (counter == J)
			break;

		parseInt(i, data);
		data[0] = data[size - 1] = 1;
		jamcoin = true;

		for (j = 2; j <= 10; j++)
		{
			ans[j-2] = check(data, j);
			
			if (ans[j - 2] == 0)
			{
				jamcoin = false;
				break;
			}
		}

		if (jamcoin)
		{
			for (j = 0; j < size; j++)
				cout << (int)data[j];
			for (j = 0; j < 9; j++)
				cout << " " << ans[j];
			cout << endl;

			counter++;
		}
	}

	return 0;
}

#endif