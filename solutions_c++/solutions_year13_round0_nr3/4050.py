#include <iostream>
#include <vector>
using namespace std;

bool isPalindrome(long long a)
{
	int digits[14], digitsCount = 0;
	while (a != 0)
	{
		digits[digitsCount] = a % 10;
		a /= 10;
		digitsCount++;
	}

	int i = 0, j = digitsCount - 1;
	while (i < j && digits[i] == digits[j])
	{
		i++, j--;
	}

	return i >= j;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	vector<long long> r;
	for (int i = 1; i <= 10000000; i++)
	{
		long long square = (long long)i * i;
		if (isPalindrome(i) && isPalindrome(square))
		{
			r.push_back(square);
		}
	}

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		long long a, b, count = 0;
		cin >> a >> b;

		int i = 0;
		while (r[i] < a) i++;
		while (r[i] >= a && r[i] <= b)
		{
			i++, count++;
		}

		cout << "Case #" << t + 1 << ": " << count << endl;
	}
	return 0;
}