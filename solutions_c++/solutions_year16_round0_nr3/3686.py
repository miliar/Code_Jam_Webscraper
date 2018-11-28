#include <iostream>
#include <string>
#include <cmath>
#include <bitset>

#define _DBG(x) std::cout << #x << "=[" << x << "]" << std::endl
#define _SHOW(x) std::cout << x << std::endl
#define _FLAG(NAME) std::cout << "FLAG " << #NAME << std::endl

using std::cout;
using std::cin;
using std::endl;
using std::string;

int getInt()
{
	int k;
	cin >> k;
	return k;
}

string getStr()
{
	string  s;
	cin >> s;
	return s;
}

int getDenom(const long a)
{
	if (a <= 2)
	{
		return (a!=2);
	}
    for(long i=2; i<sqrt(a); i++)
    {
        if(a%i == 0)
        {
			return i;
		}
    }
	return 0;
}

string Convert(int num, const int base)
{
	if (num == 0)
	{
		return "0";
	}
	string result;
	while (num > 0)
	{
		int rem = num % base;
		result = std::to_string(rem) + result;
		num /= base;
	}
	return result;
}

long getBaseValue(const long bval, const int base)
{
	long result = 0;
	long val = bval;
	for(long i=0; val > 0; i++)
	{
		if (val%2 == 1)
		{
			result += pow(base, i);
		}
		val /= 2;
	}
	return result;
}

void calc(const int id, const int len, const int samples)
{
	cout << "Case #" << id << ":" << endl;
	int resultCount = 0;
	const long maxval = pow(2, len - 2) - 1;
	long vals[9];
	for (long i = 0; i <= maxval; i++)
	{
		const long value = pow(2,len - 1) + (i * 2) + 1;
		bool isPrime = false;
		for (int j=2; j<=10; j++)
		{
			long denom = getDenom(getBaseValue(value, j));
			if (denom == 0)
			{
				isPrime = true;
				break;
			}
			vals[j-2] = denom;
		}
		if (!isPrime)
		{
			cout << Convert(value, 2);
			for (int i=2; i<= 10; i++)
			{
				cout << " " << vals[i-2];
			}
			cout << endl;
			if (++resultCount == samples)
			{
				break;
			}
		}
	}
}

int main(int argc, char** argv)
{
	const int cases = getInt();
	for (int i = 0; i < cases; i++)
	{
		const int length = getInt();
		const int samples = getInt();
		calc(i+1, length, samples);
	}
	return 0;
}
