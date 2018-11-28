#include <ios>
#include <iostream>
#include <algorithm>

int n, finalans;
bool comp[4][16] = {};
bool dp[4][16] = {};
std::string arr[4];
std::string tmp[4];
bool foundans = false;

int minimum(int a, int b)
{
	return (a < b ? a : b);
}

bool possible(int in, int s)
{
	if (in == -1 && s == 0)
		return true;
	else if (in == -1)
		return false;
	else if (!comp[in][s])
	{
		comp[in][s] = true;
		dp[in][s] = true;
		bool atleastone = false;
		for (int i = 0; i < n; i++)
		{
			if (((1 << i) & s) && (tmp[in].at(i) == '1'))
			{
				atleastone = true;
				if (!possible(in-1, s^(1 << i)))
				{
					dp[in][s] = false;
					break;
				}
			}
		}
		if (!atleastone)
			dp[in][s] = false;
	}
	return dp[in][s];
}

void ans(int in, int s, int changes)
{
	if (in == -1)
	{
		for (int i = 0; i < n*n; i++)
		{
			int ti = i/n;
			int tj = i%n;
			tmp[ti][tj] = ((((1 << i) & s) > 0) + '0');
		}
		std::sort(tmp, tmp+n);
		bool fail = false;
		do
		{
			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 16; j++)
					comp[i][j] = false;
			if (!possible(n-1, (1 << n)-1))
			{
				fail = true;
				break;
			}
		}
		while (std::next_permutation(tmp, tmp+n));
		
		if (!fail)
		{
			finalans = minimum(finalans, changes);
		}
	}
	else
	{
		int ti = in/n;
		int tj = in%n;
		if (arr[ti][tj] == '1')
			ans(in-1, s^(1 << in), changes);
		else
		{
			ans(in-1, s, changes);
			ans(in-1, s^(1 << in), changes+1);
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	std::cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		std::cin >> n;
		for (int i = 0; i < n; i++)
		{
			std::cin >> arr[i];
			tmp[i] = arr[i];
		}
		foundans = false;
		finalans = 1000000;
		ans(n*n-1, 0, 0);
		std::cout << "Case #" << t+1 << ": " << finalans << '\n';
	}
}
