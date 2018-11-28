#include<iostream>
#include<vector>
using namespace std;
FILE* pAnsF;
typedef unsigned long long ull;
vector<ull>v;
int Coin;
int J = 50;
ull GetBaseNum(ull tnum, int base)
{
	ull m = 1;
	ull basenum = 0;
	int rem;
	while (tnum)
	{
		rem = tnum % 10;
		basenum = rem*m + basenum;
		m = m*base;
		tnum = tnum / 10;
	}
	return basenum;
}
bool IsPrime(ull num, ull& divisor)
{
	bool bPrime = true;
	for (ull j = 0; j < v.size(); j++)
	{
		if (v[j] * v[j] > num)
		{
			break;
		}
		if (num % v[j] == 0)
		{
			bPrime = false;
			divisor = v[j];
			break;
		}
	}
	return bPrime;
}
void process(ull N)
{	
	for (ull i = 9; i <= N; i++)
	{
		bool bPrime = true;
		for (ull j = 0; j < v.size(); j++)
		{
			if (v[j] * v[j] > i)
			{
				break;
			}
			if (i % v[j] == 0)
			{
				bPrime = false;
				break;
			}
		}
		if (bPrime)
			v.push_back(i);
	}
}
void printPrime()
{
	for (ull i = 0; i < v.size(); i++)
	{
		cout << v[i] << endl;
	}
}
int main()
{
	freopen_s(&pAnsF, "Primes.txt", "r", stdin); 
	freopen_s(&pAnsF, "JamCoin.txt", "w", stdout);
	ull primeNum;
	for (int i = 1; i <= 78498; i++)
	{
		cin >> primeNum;
		v.push_back(primeNum);
	}
	ull baseNum = 1000000000000000;
	ull tnum=0;
	ull nTotalCombinations = 1 << 15;
	cout << "Case #1:"<< endl;
	for (ull i = 0; i < nTotalCombinations; i++)
	{
		ull m = 1;
		tnum = 0;
		for (int j = 0; j < 15; j++)
		{
			if (i & (1 << j))
			{
				tnum = m*1 + tnum;
			}
			m = m * 10;
		}
		if (tnum % 10 != 0)
		{
			tnum = tnum + baseNum;
			vector<ull>div;
			bool bJamCoin = true;
			ull divisor;
			for (int base = 2; base <= 10; base++)
			{
				ull bnum = GetBaseNum(tnum, base);
				if (IsPrime(bnum, divisor) == false)
				{
					//div.push_back(bnum); 
					div.push_back(divisor);
				}
				else
				{
					div.clear();
					bJamCoin = false;
					break;
				}
			}
			if (bJamCoin)
			{
				Coin++;
				cout << tnum << " ";
				for (int k = 1; k <= div.size(); k++)
				{
					cout << div[k - 1] << " ";
				}
				cout << endl;
			}
			if (Coin == J)
			{
				break;
			}
		}
	}
	return 0;
}
