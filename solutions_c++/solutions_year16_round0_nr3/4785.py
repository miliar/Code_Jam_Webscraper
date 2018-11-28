// future_glimpse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// include c++ headers
#include <iostream>
#include <unordered_map>
#include <map>
#include <set>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long int LLI;

bool is_prime(LLI number)
{
	if(number % 2 == 0)
	{
		return (number == 2);
	}

	LLI root = sqrt(number);
	for(LLI i=3; i<=root; i+=2)
	{
		if(number % i == 0)
		{
			return false;
		}
	}
	return true;
}

bool solve(string & s)
{
		int len = s.length();

		vector<unsigned long long> values_on_all_bases;
		for(int base=2; base<=10; base++)
		{
			unsigned long long value = 0;
			for(int i=len-1,k=0; i>=0; i--,k++)
			{
				int coff = s[i]-'0';
				value += coff*pow(base,k);
			}
			values_on_all_bases.push_back(value);
		}

		if(!any_of(values_on_all_bases.begin(), values_on_all_bases.end(), is_prime))
		{
			vector<LLI> divisors;

			for(int i=0; i<values_on_all_bases.size(); i++)
			{
				LLI num = values_on_all_bases[i];
				for(int d=2; d<num; d++)
				{
					if(num%d == 0)
					{
						divisors.push_back(d);
						break;
					}
				}
			}

			cout << s;
			for(int i=0; i<divisors.size(); i++)
			{
				cout << " "<< divisors[i];
			}
			cout << endl;
			return true;
		}
		//for(int i=0; i<values_on_all_bases.size(); i++)
		//{
		//	LLI n = values_on_all_bases[i];
		//	is_prime(n)?cout << n << " is prime\n" : cout << n << " is not prime\n";	
		//}
		return false;
}

void generate_permutations(vector<char> & set, string prefix, int n, int & j)
{
	if (j==0)
	{
		return;
	}

	if(n==0)
	{
		string s = "1" + prefix + "1";
		if(solve(s))
		{
			j--;
		}
		return;
	}

	for(int i=0; i<2; i++)
	{
		string new_prefix = prefix+set[i];
		generate_permutations(set, new_prefix, n-1,j);
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t,n,j;
	cin >> t;

	for(int i=1; i<=t; i++)
	{
		cin >> n >> j;
		vector<char> set;
		set.push_back('0');
		set.push_back('1');

		cout << "Case #"<< i << ": " << endl;
		generate_permutations(set, "", n-2,j);
 	}

	return 0;
}