#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

void incr(char* digits, int& cnt)
{
	char m = 0;
	for (int i = cnt / 2; i < cnt; i++)
	{
		char c = digits[i] + 1 + m;
		if (c < 10)
		{
			m = 0;
			digits[i] = c;
			break;
		}
		m = 1;
		digits[i] = c - 10;
	}

	digits[cnt] = m;
	cnt += m;
}

int to_digits(__int64 x, char* digits)
{
	int cnt = 0;

	do 
	{
		digits[cnt++] = x % 10;
		x /= 10;
	} while (x > 0);

	return cnt;
}

__int64 make_fair(char* digits, int cnt)
{
	__int64 n = 0;
	for (int i = 0; i < cnt; i++)
	{
		__int64 x = (i >= cnt / 2 ? digits[i] : digits[cnt - i - 1]);
		n = n * 10 + x;
	}
	return n;
}

bool is_fair(__int64 x)
{
	char digits[256];
	int cnt = to_digits(x, digits);

	for (int i = 0; i < cnt / 2; i++)
		if (digits[i] != digits[cnt - i - 1])
			return false;
	return true;
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		__int64 A, B;
		cin >> A >> B;

		__int64 q = sqrt((double)A);
		__int64 n = (q * q == A ? q : q + 1);
		__int64 result = 0;

		char digits[256];
		int cnt = to_digits(n, digits);

		while (true)
		{
			__int64 x = make_fair(digits, cnt);
			__int64 x2 = x * x;
			if(x2 >= A)
			{
				if(x2 > B)
					break;

				if (is_fair(x2))
					result++;
			}

			incr(digits, cnt);
		}

		cout << "Case #" << numCase << ": ";
		cout << result;
		cout << "\n";

		numCase++;
	}
	return 0;
}
