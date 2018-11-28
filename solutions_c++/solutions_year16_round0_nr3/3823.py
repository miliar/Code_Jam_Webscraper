#include <iostream>
#include <string>
using namespace std;
int dividors[10];
int currentBase = 0;
bool isPrime(unsigned long long number)
{
	for (unsigned long long i= 2; i <= sqrt(number); i++)
	{
		if (number % i == 0)
		{
			dividors[currentBase] = i;
			return false;
		}
			
	}
	return true;
}

void inc(string& s_num)
{
	auto lsb = s_num.length() - 1;
	int i = lsb;
	for (i = lsb; i>=0 && s_num[i] == '1'; i--)
	{
		s_num[i] = '0';
	}
	if (i >= 0)
	{
		s_num[i] = '1';
	}
	s_num[0] = '1';
	s_num[lsb] = '1';
}

unsigned long long power(int num,int power)
{
	unsigned long long result = 0;
	if (num > 0)
	{
		result = 1;
	}
	for (int i = 0; i < power; i++)
	{
		result *= num;
	}
	return result;
}

bool testBase(string s_num, int base)
{
	auto lsb = s_num.length() - 1;
	int i = lsb;
	unsigned long long result = 0;
	for (i = lsb; i >= 0 ; i--)
	{
		if (s_num[i] == '1')
		{
			result += power(base , (lsb  - i));
		}
	}
	currentBase = base;
	return isPrime(result);
}



int main(char* argv, int argc)
{
	int cases = 0;
	cin >> cases;
	for (int i = 1; i <= cases; i++)
	{
		int N, J;
		cin >> N;
		cin >> J;
		string s_num = "";
		bool coinJam = true;
		for (int i = 0; i < N; i++)
		{
			s_num += "0";
		}
		s_num[N - 1] = '1';
		s_num[0] = '1';
		cout << "Case #" << (i) << ":" << endl;
		while (J>0)
		{
			coinJam = true;
			for (int k = 2; k <= 10; k++)
			{
				if (testBase(s_num, k))
				{
					coinJam = false;
					break;
				}
			}
			if (coinJam)
			{
				cout << s_num << " ";
				for (int x = 2; x <= 10; x++)
					cout << dividors[x] << " ";
				cout << endl;
				J--;
			}
			inc(s_num);
		}
	}

}