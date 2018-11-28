#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

unsigned long int isPrime(unsigned long long int num)
{
	if (num <= 1)
		return 1;
	else if (num == 2)
		return 0;
	else if (num % 2 == 0)
		return 2;
	else
	{
		long int prime = 0;
		long int divisor = 3;
		double num_d = static_cast<double>(num);
		long int upperLimit = min(static_cast<long int>(sqrt(num_d) + 1), static_cast<long int>(32000));

		while (divisor <= upperLimit)
		{
			if (num % divisor == 0)
			{
				prime = divisor;
				break;
			}
			divisor += 2;
		}
		return prime;
	}
}

unsigned long long int toDecimal(string s, int base)
{
	unsigned long long int result = 0;
	for (int i = 0,j = s.length()-1;j>=0; i++,j--)
		if (s[j] == '1')
			result += (unsigned long long int)pow((double)base, (double)i);
	return result;
}

string fromDecimal(unsigned long long int n, int base)
{
	string res;
	while (n >= base)
	{
		res += to_string(n%base);
		n = n / base;
	}
	if (n != 0) res += to_string(n);
	reverse(res.begin(),res.end());
	return res;
}

int main()
{
	ifstream in("C-small-attempt2.in");
	ofstream out("C-small-attempt2.out");

	int numberOfTests;
	in >> numberOfTests;

	for (int t = 1; t <= numberOfTests; t++)
	{	
		int N, J;
		in >> N >> J;

		string s(N,'0');
		s[0] = '1';
		s[s.length() - 1] = '1';

		unsigned long long int min;
		
		min = toDecimal(s, 2);		
		out << "Case #" << t << ": "<<endl;

		while (J > 0)
		{
			int arrOfDividers[9];
			bool isP = false;
			string buf = fromDecimal(min, 2);

			for (int base = 2; base <= 10; base++)
			{				
				unsigned long long int bufDec = toDecimal(buf, base);
				unsigned long long int divisor = isPrime(bufDec);
				if (divisor != 0)
					arrOfDividers[base - 2] = divisor;
				else
				{
					isP = true;
					break;
				}
			}
			if (!isP)
			{
				out << fromDecimal(min, 2) << " ";
				for (int i = 0; i < 9; i++)
					out << arrOfDividers[i] << " ";
				out << endl;
				J--;
			}
			min += 2;			
		}


	}

	return 0;
}







