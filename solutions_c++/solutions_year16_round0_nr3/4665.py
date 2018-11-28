#include <sstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

unsigned long long int divisors[11];
unsigned long long int lastdivisor;

bool isprime(unsigned long long int i)
{
	unsigned long long int j;
	if ( i == 0 )
	{
		return false;
	}
	if ( i == 1 )
	{
		return false;
	}
	if ( i == 2 )
	{
		return true;
	}
	if ( i%2 == 0 )
	{
		lastdivisor = 2;
		return false;
	}
	for ( j=3;j<=sqrt((double)i)+1;j+=2 )
	{
		if ( i%j == 0 )
		{
			lastdivisor = j;
			return false;
		}
	}
	return true;
}

int verifycoin(unsigned long long int coin)
{
	std::ostringstream ss;
	unsigned long long int number;
	int base;
	int result = 1;
	string str;
	//cout << "entering" << endl;
	for (base=2;base<=10;base++)
	{
		ss.str("");
		ss.clear();
		ss << coin;
		//str = to_string(coin);
		//cout << "ss: " << ss.str() << endl;
		number = strtoll(ss.str().c_str(), NULL, base);
		//cout << "base: " << base << ", number: " << number << endl;
		if ( isprime(number) )
		{
			result = 0;
			break;
		}
		else
		{
			divisors[base] = lastdivisor;
		}
		//cout << "number: " << number << endl;
	}
	return result;
}

int main(void)
{
	int T;
	int N;
	int J;
	int j;
	int found;
	int mult;
	unsigned long long int jamcoin;
	
	// T is always 1..
	cin >> T;
	cin >> N;
	cin >> J;
	
	cout << "Case #1:" << endl;
	found = 0;
	// create first possible jamcoin
	jamcoin = 1;
	for (int i=1;i<N;i++)
	{
		jamcoin = jamcoin*10;
	}
	jamcoin++;
	while (found<J)
	{
		if ( verifycoin(jamcoin) )
		{
			cout << jamcoin;
			for (int i=2;i<=10;i++)
			{
				cout << " " << divisors[i];
			}
			cout << endl;
			found++;
		}
		
		// go to next possible jamcoin
		mult = 10;
		jamcoin = jamcoin + mult;
		while ( (jamcoin/mult)%10 > 1 )
		{
			jamcoin = jamcoin - 2*mult;
			mult=mult*10;
			jamcoin = jamcoin + mult;
		}
		//cout << "trying: " << jamcoin << endl;
	}	
	
	return 0;
}