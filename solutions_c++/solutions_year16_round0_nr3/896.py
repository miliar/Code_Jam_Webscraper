#include <iostream>
#include <string>
#include<vector>

using namespace std;

unsigned long long divisor(unsigned long long number)
{
	unsigned long long div = 2;
	unsigned long long sqrtNumber = (unsigned long long)sqrt(number);
	while (number % div != 0 && div <= sqrtNumber)
		++div;
	if (div > sqrtNumber)
		return 0;
	return div;
}

unsigned long long convertToBase(string s, int base)
{
	unsigned long long output = 0;
	int len = s.length();
	for (int i = 0; i < len; ++i)
	{
		if (s.at(len - 1 - i) == '1')
			output += (unsigned long long)pow(base, i);
	}
	return output;
}

string intToRevBinaryString(int b, int len)
{
	string s;
	for (int i = 0; i < len; ++i)
	{
		s += (b % 2) + '0';
		b /= 2;
	}
	return s;
}

void run()
{
	int N, J;
	cin >> N >> J;

	vector<unsigned long long> divisors;

	int maxB = (int)pow(2, N - 2) - 1;
	int found = 0;
	for (int b = 0; b < maxB && found < J; ++b)
	{
		string s = "1" + intToRevBinaryString(b, N - 2) + "1";
		divisors.clear();

		for (int base = 2; base <= 10; ++base)
		{
			unsigned long long div = divisor(convertToBase(s, base));
			if (div == 0)
				break;

			divisors.push_back(div);
		}

		if (divisors.size() == 9)
		{
			cout << s;
			for (size_t i = 0; i < divisors.size(); ++i)
				cout << " " << divisors[i];
			cout << endl;
			++found;
		}
	}
}

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ":" << endl;
		run();
	}
}