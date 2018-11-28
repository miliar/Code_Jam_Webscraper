#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int Solve(unsigned long long A, unsigned long long B);
bool IsPalindrome(unsigned long long num);

int main()
{
	int T;
	unsigned long long A, B;
	char strBuff[204];

	char** board = new char*[4];
	for (int i = 0; i < 4; i++)
		board[i] = new char[4];
	


	ifstream fin;
	fin.open("C.txt", ifstream::in);

	ofstream fout;
	fout.open("Output.txt", ofstream::out);

	fin.getline(strBuff, 203);

	sscanf(strBuff, "%d", &T);

	for (int i = 0; i < T; i++)
	{
		fout << "Case #" << (i+1) << ": ";

		fin.getline(strBuff,203);

		sscanf(strBuff, "%llu %llu", &A, &B);

		fout << Solve(A, B) << "\n";

	}
	fout.close();
	
	fin.close();

//	cin.get();
}

int Solve(unsigned long long A, unsigned long long B)
{
	int total = 0;

	unsigned long long start = ceil(sqrt((long double)A));
	unsigned long long end = floor(sqrt((long double)B));

	for (unsigned long long i = start; i <= end; i++)
	{
		if (IsPalindrome(i))
		{
			if (IsPalindrome(pow(i, 2.0))) total++;
		}
	}

	return total;
}

bool IsPalindrome(unsigned long long num)
{
	int digits[15];
	int nDigits;

	for (int i = 0; i < 15; i++)
	{
		digits[i] = num % 10;
		num /= 10;
		if (num == 0) 
		{
			nDigits = i;
			break;
		}
	}

	for (int i = 0; i < nDigits; i++)
	{
		if (digits[i] != digits[nDigits - i]) return false;
	}

	return true;
}