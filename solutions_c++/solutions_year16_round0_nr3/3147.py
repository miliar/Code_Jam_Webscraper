#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;

long long int charToBaseAny(char* base2Char, int base);
long long int checkDivisor(long long int in);

int main(void)
{
	ifstream file;
	file.open("C-small-attempt0.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for (int t = 1; t <= caseNo; t++)
	{
		int n, j;
		file >> n >> j;

		output << "Case #" << t << ":" << endl;

		long long int base2;
		if (n == 16) base2 = 0x8001;
		else if (n == 32) base2 = 0x80000001;

		char base2Char[33];

		int count = 0;
		while (count < 50)
		{
			itoa(base2, base2Char, 2);
			string outputStr = "";
			bool isJamcoin = true;

			outputStr += base2Char;
			outputStr += " ";
			for (int tt = 2; tt <= 10; tt++)
			{
				long long int temp;
				long long int divisor;
				temp = charToBaseAny(base2Char, tt);
				divisor = checkDivisor(temp);
				if (divisor != temp)
				{
					char temp[33];
					itoa(divisor, temp, 10);
					outputStr += temp;
					outputStr += " ";
				}
				else isJamcoin = false;
			}

			if (isJamcoin == true)
			{
				count++;
				output << outputStr << endl;
			}

			base2 += 0x2;
		}

	}
}

long long int charToBaseAny(char base2[], int base)
{
	int size = strlen(base2);
	long long int result = 0;
	for (int t = size - 1; t >= 0; t--)
	{
		if (base2[size - t - 1] == '1') result += pow(base, t);
	}
	return result;
}

long long int checkDivisor(long long int in)
{
	for (long long int x = 2; x <= 100000; x++)
	{
		if (in % x == 0) return x;
	}
	return in;
}