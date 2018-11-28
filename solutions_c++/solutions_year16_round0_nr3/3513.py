#include <bits/stdc++.h>

typedef long long ll;

std::vector <int> prime;

struct status
{
	std::vector <int> list;
	int divisors[11];

	inline void print()
	{
		for (int i = 0; i < (int)list.size(); i ++)
			std::cout << list[i];
		for (int i = 2; i <= 10; i ++)
			std::cout << " " << divisors[i];
		std::cout << std::endl;
	}
};

inline void get_prime()
{
	std::bitset <40000010> is_prime;
	for (int i = 2; i <= 40000000; i ++)
		if (!is_prime[i])
		{
			prime.push_back(i);
			for (int j = i; j <= 40000000; j += i)
				is_prime.set(j);
		}
}

inline int is_prime(ll x)
{
	int ans = -1;
	for (int i = 0; i < (int)prime.size() && prime[i] <= x; i ++)
		if (x % prime[i] == 0 && x != prime[i])
		{
			ans = prime[i];
			break;
		}
	return ans;
}

int main()
{
	get_prime();
	std::ios::sync_with_stdio(false);
	int T;
	std::cin >> T;
	for (int Case = 1; Case <= T; Case ++)
	{
		std::cout << "Case #" << Case << ":" << std::endl;
		int n, m;
		std::cin >> n >> m;
		std::vector <status> list;
		for (int i = 0; i < (1 << (n - 2)); i ++)
		{
			status ans;
			ans.list.push_back(1);
			for (int j = 0; j < n - 2; j ++)
				if (i & (1 << j))
					ans.list.push_back(1);
				else
					ans.list.push_back(0);
			ans.list.push_back(1);
			bool flag = true;
			for (int j = 2; j <= 10; j ++)
			{
				ll base = 1, sum = 0;
				for (int k = n - 1; k >= 0; k --)
				{
					sum += ans.list[k] * base;
					base *= j;
				}
				int tmp = is_prime(sum);
				if (tmp == -1)
				{
					flag = false;
					break;
				}
				ans.divisors[j] = tmp;
			}
			if (flag)
				list.push_back(ans);
			if ((int)list.size() == m)
				break;
		}
		for (int i = 0; i < (int)list.size(); i ++)
			list[i].print();
	}
	return 0;
}
