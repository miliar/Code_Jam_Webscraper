#include <vector>
#include <iostream>

std::vector<std::pair<bool, bool> > a;

bool is_palindrome(int n)
{
	int x = n;
	int reversed = 0;
	while (x)
	{
		(reversed *= 10) += (x % 10);
		x /= 10;
	}
	return n == reversed;
}

int count(int x, int y)
{
	int result = 0;
	for (int i = x; i <= y; ++i)
	{
		result += a[i].first && a[i].second;
	}
	return result;
}

int main()
{
	a = std::vector<std::pair<bool, bool> > (1001, std::make_pair(false, false));
	for (int i = 1; i < 1001; ++i)
	{
		a[i].first = is_palindrome(i);
		if (i * i < 1001)
		{
			a[i * i].second = a[i].first;
		}
	}
	int t;
	std::cin >> t;
	for (int i = 0; i < t; ++i)
	{
		int x, y;
		std::cin >> x >> y;
		std::cout << "Case #" << i + 1 << ": " << count(x, y) << std::endl;
	}
	return 0;
}
