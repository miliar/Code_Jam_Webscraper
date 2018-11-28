#include <iostream>
#include <cmath>

using namespace std;

int ndigit(long long no, int index)
{
	return ((no / (long long)pow(10, index - 1)) % 10);
}

bool isPalindrome(long long no)
{
	if (no < 10)
	{
		return true;
	}
	int digits = 1;
	long long temp = no;
	for (; temp/10 != 0; temp /= 10, digits++);
	for (int i = 1; i <= digits/2; i++)
	{
		if (ndigit(no, i) != ndigit(no, digits - i + 1))
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long a, b;
		cin >> a;
		cin >> b;

		long long asqrt, bsqrt;
		asqrt = (long long)ceil(sqrt(a));
		bsqrt = (long long)floor(sqrt(b));

		int count = 0;
		for (long long j = asqrt; j <= bsqrt; j++)
		{
			if (isPalindrome(j) && isPalindrome(j * j))
			{
				count++;
			}
		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}
	return 0;
}
