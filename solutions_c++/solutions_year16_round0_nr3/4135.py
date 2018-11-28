#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <math.h>
#include <bitset>

using namespace std;

bool checkPrime(long long num)
{
	if (num == 0)
	{
		return true;
	}
	if (num < 2 || num%2==0)
	{
		return false;
	}
	for (long long i = 3; i <= sqrt(num); i+=2)
	{
		if (num%i == 0)
		{
			return false;
		}
	}
	return true;
}

std::vector<std::string> getBitStrings(unsigned int n)
{
	std::vector<std::string> result;

	if (n <= 1)
	{
		result.push_back("0");
		result.push_back("1");
	}
	else
	{   // recurse, then add extra bit chars
		std::vector<std::string> sub = getBitStrings(n - 1);
		for (std::vector<std::string>::const_iterator it = sub.cbegin();
			it != sub.cend(); ++it)
		{
			result.push_back(*it + '0');
			result.push_back(*it + '1');
		}
	}
	return result;
}


long long convertToBase(string binaryNum, int base)
{
	long long result = 0;
	int n = 0;
	for (int i = binaryNum.size()-1; i >= 0; i--)
	{
		result += ((binaryNum[i] - '0') * pow(base, n));
		n++;
	}
	return result;
}
long long GetDivisor(long long num)
{
	for (long long x = 2; x < num; x++)
	{
		if (num%x == 0)
		{
			return x;
		}
	}
	return 0;
}

vector<string> GetVariations(int n)
{
	vector<string> results = getBitStrings(n - 2);

	for (int i = 0; i < results.size(); i++)
	{
		results[i] = ("1" + results[i] + "1");
	}
	return results;
}

int main()
{
	fstream fin;
	fstream fout;
	fin.open("C-small-attempt1.in", ios::in);
	fout.open("C-small-attempt1.out", ios::out);
	
	int t;
	fin >> t;

	for (int i = 0; i < t; i++)
	{
		int n, j;
		fin >> n >> j;
		vector<string> jamcoins;
		jamcoins = GetVariations(n);
		int count = 0;
		fout << "Case #" << (i + 1) <<":"<< endl;
		for (int k = 0; k < jamcoins.size() && j > 0; k++)
		{
			bool check = false;
			
			for (int b = 2; b <= 10; b++)
			{
				long long rep = convertToBase(jamcoins[k], b);
				if (checkPrime(rep))
				{
					check = true;
					break;
				}
			}
			if (!check)
			{
				fout << jamcoins[k] << " ";
				for (int b = 2; b <= 10; b++)
				{
					long long rep = convertToBase(jamcoins[k], b);
					fout << GetDivisor(rep) << " ";
				}
				fout << endl;
				j--;
			}
		}

	}
	return 0;
}