#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <math.h>
#include <map>
#include <vector>
#include <fstream>
using namespace std;
int primes[] =
{
	2, 3, 5, 7, 11, 13, 17, 19
};
long long samplenotprime[] =
{
	1000000000000001,	1000000000000011,	1000000000000101,	1000000000000111,	1000000000001001,	1000000000001101,	1000000000001111,	1000000000010001,
	1000000000010011,	1000000000010101,	1000000000010111,	1000000000011001,	1000000000011011,	1000000000011111,	1000000000100001,	1000000000100101,
	1000000000100111,	1000000000101001,	1000000000101011,	1000000000101111,	1000000000110001,	1000000000110011,	1000000000110101,	1000000000110111,
	1000000000111001,	1000000000111011,	1000000000111101,	1000000000111111,	1000000001000001,	1000000001000011,	1000000001000111,	1000000001001001,
	1000000001001011,	1000000001001101,	1000000001001111,	1000000001010001,	1000000001010011,	1000000001010101,	1000000001010111,	1000000001011001,
	1000000001011011,	1000000001011101,	1000000001011111,	1000000001100001,	1000000001100011,	1000000001100101,	1000000001100111,	1000000001101001,
	1000000001101011,	1000000001101101,
	1000000001101111,	1000000001110001,	1000000001110011,	1000000001110101,	1000000001110111,	1000000001111001,	1000000001111011,	1000000001111101,
	1000000001111111,	1000000010000001,	1000000010000011,	1000000010000101,	1000000010000111,	1000000010001001,	1000000010001101,	1000000010001111,
	1000000010010001,	1000000010010101,	1000000010010111,	1000000010011001,	1000000010011011,	1000000010011101,	1000000010011111,	1000000010100001,
	1000000010100011,	1000000010100101,	1000000010100111,	1000000010101001,	1000000010101011,	1000000010101101,	1000000010110011,	1000000010110101,
	1000000010111001,	1000000010111011,	1000000010111101,	1000000011000001,	1000000011000011,	1000000011000101,	1000000011000111,	1000000011001011,
	1000000011001101,	1000000011010001,	1000000011010011,	1000000011010101,	1000000011010111,	1000000011011001,	1000000011011011,	1000000011011101,
	1000000011011111,	1000000011100001,	1000000011100011,	1000000011100101,	1000000011100111,	1000000011101001,	1000000011101111,	1000000011110001,
	1000000011110011,	1000000011110101,	1000000011110111,	1000000011111001
};
bool IsPrime(long long number)
{	
	for (long i = 0; i<=10008; i++)
	{
		if (number % primes[i] == 0)
		{
			if (primes[i] != number)
			{
				return false;
			}
		}
	}
	for (long long i = 1299827; i < sqrt(number); i++)
	{
		if (number % i == 0)
		{
			return false;
		}
	}
	return true;
}
long long tobasen(long long number,int base)
{
	long long x = number;
	ostringstream bin;
	long long r;
	while (x != 0)
	{
		r = x % base;
		x = x / base;;
		bin << r;
	}
	string g = bin.str();
	reverse(g.begin(), g.end());
	return stoll(g);
}
long long interpret(long long number, int base)
{
	long long o = 0;
	ostringstream tmp;
	tmp << number;
	string s = tmp.str();
	for (int i = s.size() - 1; i >= 0; i--)
	{
		if (s[i] == '1')
		{
			o = o + pow(base, s.size()-1-i);
		}
	}
	return o;
}
int main()
{
	ifstream input;
	ofstream output;
	ifstream binary;
	fstream rules;
	vector<string> binaryv;
	input.open("A-large.in");
	binary.open("binary.txt");
	rules.open("rules.txt",ios::out|ios::in);
	output.open("test.on");
	vector<long long> u;
	for (int k = 0; k < 110; k++)
	{
		long long sample = samplenotprime[k];
		//output << samplenotprime[k] << " : " << IsPrime(samplenotprime[k]) << endl;
		int count = 0;
		for (int i = 2; i < 10; i++)
		{			
			long long base = interpret(sample, i);
			if (!IsPrime(base))
			{
				count++;
			}
		}
		
		if (count == 8)
		{
			rules << samplenotprime[k]<<endl;
			u.push_back(samplenotprime[k]);
		}
	}
	output << "Case #1:" << endl;
	vector<long long> taken;
	long long tmp,temp;
	for (int i = 0; i < 50; i++)
	{
		output << u[i];
		//cout << u[i];
		for (int k = 2; k <= 10; k++)
		{
			tmp = interpret(u[i], k);
			for (long long l = 2; l < sqrt(tmp); l++)
			{
				if (tmp % l == 0)
				{
					if (find(taken.begin(), taken.end(), l) == taken.end())
					{
						output <<" " << l;
						//cout << " " << l;
						taken.push_back(l);
						break;
					}
					else if (find(taken.begin(), taken.end(), tmp/l) == taken.end())
					{
						output << " " << tmp/l;
						//cout << " " << tmp/l;
						taken.push_back(tmp/l);
						break;
					}
				}
			}
		}
		if (i != 49) { output << endl;  /*cout << endl;*/ }
	}
	return 0;
}
