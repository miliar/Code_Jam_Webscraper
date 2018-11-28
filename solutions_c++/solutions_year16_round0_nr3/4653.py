#include <iostream>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

bool isPrime(long long &x)
{
	if (x == 0 || x == 1)
	{
		return false;
	}
	for (int i = 2; i <= sqrt(x);i++)
	{
		if (x%i == 0)
			return false;
	}
	return true;
}

long long base_to_dec(string s, int base)
{
	long long dec_value=0;
	int n = s.length();
	for (int i = 0; i < n ;i++)
	{
		if (s[i] == '1') dec_value += pow(base  ,(n - 1 - i));
	}
	return dec_value;
}

int middle_to_dec(string s, int base)
{
	int dec_value = 0;
	int n = s.length();
	for (int i = 0; i < n;i++)
	{
		if (s[i] == '1') dec_value += pow(base, (n - i));
	}
	return dec_value;
}

bool isJamcoin(string comb , int N)
{
	for (int base = 2; base <= 10; base++)
	{
		long long d_value = middle_to_dec(comb, base);
		//d_value= d_value << 1;
		d_value += pow(base, N - 1) + 1;

		if (isPrime(d_value))
		{
			//this comb can't be a jamcoin
			return false;
		}
	}
	return true;
}

int get_divisor(long long value)
{
	for (int k = 2; k < value;k++)
	{// loop till a divisor found

		if (value%k == 0)
		{
			return k;
		}
	}
	
		return 0;
}
int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;

	int N, J;
	cin >> N >> J;
	
	// generate combinations 
	vector<string> jamcoins;
	int a = pow(2,N-2)-1; // max value that can be represented in the middle N-2 digits
	
	for (int i = 0; i <= a;i++)
	{
		bitset<14> bin(i); // for small data set
		string comb = bin.to_string();


		if (isJamcoin(comb, N))
		{
			int  comb_dvalue = (base_to_dec(comb,2)<<1) +pow(2, N - 1) + 1;
			bitset<16> c(comb_dvalue);
			string temp = c.to_string();
			jamcoins.push_back(temp);
		}
	
		if (jamcoins.size() == J)  
		{
			break;
		}
		
	}
	
	
	cout << "Case #1: " << endl;

	// generate divisors 
	for (int j = 0; j < jamcoins.size(); j++)
	{ // for each jamcoin

		cout<<jamcoins[j]<<" ";

		for (int base = 2; base <= 10; base++)
		{ // for each base

			long long value = base_to_dec(jamcoins[j], base);

			bool flag = false;
			int div=get_divisor(value);
			cout << div << " ";
		}
		cout << endl;
	}

	return 0;
}
