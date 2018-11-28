#include<stdio.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
using namespace std;

void Check(string str);
long long int IsPrimeOrNTD(long long int number);
long long int Calc(string s, long long int k);
void Recur(int p, string str);

int done = 0;
int n = 16;
int maxJ = 50;

ifstream in;
ofstream out;

int main()
{
	//ifstream in("B-large.in");
	in.open("in.txt");
	out.open("out.txt");
	//out << "Case #1:" << endl;

	Recur(2, "1000000000000001");

	//out << ": " << result << endl;

	in.close();
	out.close();
	return 0;
}

void Recur(int p, std::string str)
{
	if (p >= n)
	{
		Check(str);
		return;
	}

	for (int j = 0; j < 2; ++j)
	{
		str[p - 1] = (j + '0');
		Recur(p + 1, str);
		if (done >= maxJ)
			return;
	}
}

void Check(string str)
{
	long long int result;
	long long int ntd[11] = { 0, };
	for (long long int k = 2; k <= 10; ++k)
	{
		// 1001 = str
		// 9 28 65 126 217 344 513 730 1001     = result
		// 2 3  4  5   6   7   8   9   10  진수 = k

		result = Calc(str, k);

		long long int ntdntd = IsPrimeOrNTD(result);

		// prime number면 제낀다.
		// non-trivial divisor 없으면 제낀다.
		if (ntdntd <= 0)
			return;

		ntd[k] = ntdntd;
	}

	done++;

	out << str << " ";
	for (int k = 2; k <= 10; ++k)
	{
		out << ntd[k];
		if (k < 10)
			out << " ";
	}
	out << endl;
}

long long int IsPrimeOrNTD(long long int number)
{
	bool isPrime = true;
	long long int sq = (long long int)sqrt(number);
	for (int i = 2; i <= sq; ++i)
	{
		if (number % i == 0)
		{
			isPrime = false;
			// non-trivial divisor 가 있다.
			if (i % 2 == 1 || (number / i) % 2 == 1)
				return i;
		}
	}

	if (isPrime) // 아예 prime number면 -1
		return -1;
	return 0; // prime number가 아니지만, non-trivial divisor가 없는 경우 0
}

long long int Calc(string s, long long int k)
{
	long long int result = 0;
	long long int temp = 1;
	for (int i = s.length() - 1; i >= 0; --i)
	{
		if (s[i] == '1')
			result += temp;
		temp *= k;
	}
	return result;
}