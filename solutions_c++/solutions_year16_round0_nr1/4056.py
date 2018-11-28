#include <bits/stdc++.h>

std::bitset <10> to_digit(int x)
{
	std::bitset <10> ans;
	if (!x)
		ans.set(0);
	else
	{
		while (x)
		{
			ans.set(x % 10);
			x /= 10;
		}
	}
	return ans;
}

int main()
{
	std::ios::sync_with_stdio(false);
	int T;
	std::cin >> T;
	for (int Case = 1; Case <= T; Case ++)
	{
		std::cout << "Case #" << Case << ": ";
		int n;
		std::cin >> n;
		if (!n)
		{
			std::cout << "INSOMNIA" << std::endl;
			continue;
		}
		int ans;
		std::bitset <10> tmp;
		for (int i = 1; i <= 100; i ++)
		{
			tmp |= to_digit(i * n);
			if ((int)tmp.count() == 10)
			{
				ans = i;
				break;
			}
		}
		std::cout << n * ans << std::endl;
	}
	return 0;
}
