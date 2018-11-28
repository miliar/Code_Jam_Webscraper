#include <bits/stdc++.h>

using namespace std;

const int MAXN = 10000010;
bool mark[MAXN];
vector<int> primes;
vector<int> divisors;

inline long double convertBase(long long mask, int b)
{
	long double tmp = 0, p = 1;
	while (mask)
	{
		tmp = (tmp + (mask & 1) * p);
		mask /= 2;
		p = (p * b);
	}
	return tmp;
}

inline int div(long long mask, int b)
{
	long long mask2 = mask;
	long double cb = convertBase(mask2, b);
	for (int i = 0; i < (int)primes.size(); i++)
	{
		long long mod = primes[i];
		long long tmp = 0;
		long long p = 1;
		mask = mask2;
		while (mask)
		{
			tmp = (tmp + (mask & 1) * p);
			while (tmp >= mod)
				tmp -= mod;
			mask /= 2;
			p = (p * b);
			while (p >= mod)
				p -= mod;
		}
		if ((long double)mod * (long double)mod > cb)
			break;
		if (tmp == 0)
			return primes[i];
	}
	return -1;
}


int main()
{
	mark[1] = true;
	for (int i = 1; i < MAXN; i++)
		if (!mark[i])
			for (int j = 2 * i; j < MAXN; j += i)
				mark[j] = true;
	for (int i = 1; i < MAXN; i++)
		if (!mark[i])
			primes.push_back(i);
	int cnt = 0;
	cout << "Case #1:" << endl;
	for (long long mask = 0; mask < (1ll << 30); mask++)
	{
		long long mask2 = (mask + (1ll << 30)) * 2ll + 1ll;
		divisors.clear();
		for (int i = 2; i <= 10; i++)
		{
			int d = div(mask2, i);
			if (d != -1)
				divisors.push_back(d);
			else
				break;
		}
		if (divisors.size() == 9)
		{
			cout << bitset<32>(mask2) << " ";
			for (int i = 0; i < 9; i++)
				cout << divisors[i] << " \n"[i == 8];
			cnt++;
			if (cnt == 500)
				break;			
		}
	}
	return 0;
}