#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

ofstream output;
int J, jCount = 0;

void stringBuffer(string str, int len, int n);
void appendString(string& str, int len);
inline bool isPrime(unsigned long long number);
void checkNumber(string str);
int tellDivisor(unsigned long long num);

int main()
{
	int T, N;
	string fileName;
	string str;

	ifstream input;

	cout << "File name : ";
	getline(cin, fileName);

	input.open(fileName + ".in");
	output.open(fileName + ".out");

	input >> T;

	for (int i = 0; i < T; i++)
	{
		input >> N >> J;

		appendString(str, N);
		output << "Case #" << i + 1 << ": " << endl;
		stringBuffer(str, N, N - 1);
	}

	output.close();

	return 0;
}

inline bool isPrime(unsigned long long number)
{
	for (register unsigned i = 2; i <= sqrt(number); ++i)
	{
		if (number % i == 0) return false;
	}
	return true;
}


void stringBuffer(string str, int len, int n)
{
	if (n > 1)
	{
		str.at(len - n) = '0';

		stringBuffer(str, len, n - 1);

		str.at(len - n) = '1';

		stringBuffer(str, len, n - 1);
	}
	else
		checkNumber(str);
}

void appendString(string& str, int len)
{
	for (int i = 1; i < len - 1; i++)
		str += '.';

	str.insert(str.begin(), '1');
	str.insert(str.end(), '1');
}

void checkNumber(string str)
{
	if (jCount < J)
	{
		for (int i = 2; i <= 10; i++)
			if (isPrime(stoull(str, 0, i)))
				return;

		output << str << " ";

		for (int j = 2; j <= 10; j++)
			output << tellDivisor(stoull(str, 0, j)) << " ";

		output << endl;
		jCount++;
	}
}

int tellDivisor(unsigned long long num)
{
	for (register unsigned i = 2; i <= sqrt(num); i++)
		if (num % i == 0)
			return i;
}