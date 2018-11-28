#include <fstream>
#include <cmath>
#include <iostream>

using namespace std;

long long int binToDeci(int ident[32], int &N);
long long int isPrime(int ident[32], int base, long long int& limit, int& N);
void newIdent(int ident[32], int& N);
void toBinary(int ident[32], long long int& number, int& N);
bool isDivisible(int ident[32], int& base, long long int& divisor, int& N);

int main()
{
	ifstream input;
	ofstream output;
	
	input.open("C-large.in");
	output.open("output.txt");
	
	int T, N, J;
	struct Coin
	{
		int ident[32];
		long long int divisors[9];
		long long int limits[9];
	} myCoin;
	
	input >> T;
	
	output << "Case #" << 1 << ":" << endl;
	input >> N >> J;
	
	myCoin.ident[0] = 1;
	for(int i = 1; i < N - 1; i++)
	{
		myCoin.ident[i] = 0;
	}
	myCoin.ident[N-1] = 1;
	for(int b = 0; b < 9; b++)
	{
		myCoin.limits[b] = 50000;
	}
	bool test;
	for(int j = 1; j <= J; j++)
	{
		test = true;
		for(int b = 0; b < 9 && test; b++)
		{
			myCoin.divisors[b] = isPrime(myCoin.ident, b, myCoin.limits[b], N);
			if(myCoin.divisors[b] == 0)
			{
				test = false;
				j--;
			}
		}
		if(test)
		{
			for(int i = 0; i < N; i++)
			{
				output << myCoin.ident[i];
			}
			for(int i = 0; i < 9; i++)
			{
				output << " " << myCoin.divisors[i];
			}
			output << endl;
		}
		newIdent(myCoin.ident, N);
	}
	
	
	input.close();
	output.close();
	
	return 0;
}

long long int binToDeci(int ident[32], int &N)
{
	long long int counter, number;
	counter = 1;
	number = 0;
	for(int i = N-1; i >= 0; i--)
	{
		number += ident[i] * counter;
		counter *= 2;
	}
	return number;
}

long long int isPrime(int ident[32], int base, long long int& limit, int& N)
{
	long long int result = 2;
	
	if(isDivisible(ident, base, result, N))
	{
		return 2;
	}
	result = 0;
	for(long long int i = 3; i <= limit; i+= 2)
	{
		//cout << i << endl;
		if(isDivisible(ident, base, i, N))
		{
			result = i;
			return result;
		}
	}
	return result;
}

void newIdent(int ident[32], int& N)
{
	long long int number = binToDeci(ident, N);
	number += 2;
	toBinary(ident, number, N);
	return;
}

void toBinary(int ident[32], long long int& number, int& N)
{
	int result;
	int counter = N - 1;
	while(number > 0)
	{
		ident[counter] = number % 2;
		number /= 2;
		counter--;
	}
	return;
}

bool isDivisible(int ident[32], int& base, long long int& divisor, int& N)
{
	long long int value = 0;
	for(int i = 0; i < N; i++)
	{
		value *= base + 2;
		value += ident[i];
		value %= divisor;
	}
	if(value == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}
