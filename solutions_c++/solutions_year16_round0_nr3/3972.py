#include <fstream>
#include <iostream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;
vector<bool> jamcoin;
ifstream in("C-small-attempt0.in");
ofstream out("1.txt");

long long isprime(long long x)
{
	long long n = sqrt(x) + 0.5;
	for (long long i = 2; i <= n; i++)
		if (x % i == 0)
			return i;
	return 0;
}

void add()
{
	vector<bool> jamcoin1 = jamcoin;
	int k = 1;
	while (jamcoin1[k])
	{
		jamcoin[k] = !jamcoin[k];
		k++;
	}
	jamcoin[k] = !jamcoin[k];
}

bool judge(int n)
{
	int i, k;
	long long sol, count;
	vector<long long> num;
	for (k = 2; k <= 10; k++)
	{
		sol = 0;
		for (i = 0; i < n; i++)
		{
			if (jamcoin[i])
				sol += pow(k, i);
		}
		count = isprime(sol);
		if (count !=0)
		{
			num.push_back(count);
		}
		else
			return true;
	}
	out << sol << " ";
	for (k = 0; k < 8; k++)
		out << num[k] << " ";
	out << num[8] << endl;
	return false;
}

void jam_coin(int n, int j)
{
	int k;
	jamcoin.clear();
	jamcoin.resize(n);
	for (k = 0; k < n; k++)
		jamcoin[k] = false;
	jamcoin[0] = true;
	jamcoin[n - 1] = true;
	for (k = j; k > 0; k--)
	{
		while (judge(n))
		{
			add();
		}
		add();

	}
}

int main()
{
	int T, i, j, n;
	in >> T;
	for (i = 0; i < T; i++)
	{
		out << "Case #" << i + 1 << ":"<<endl;
		in >> n >> j;
		jam_coin(n, j);
	}
	return 0;
}