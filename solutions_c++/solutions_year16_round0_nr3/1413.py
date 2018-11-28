#include <iostream>
#include <vector>
#include <cmath>

#define ULL unsigned long long

using namespace std;

string make_coinjam(int coinjam);

int main()
{
	int N = 16, J = 50;
	int maxx = 1 << 14;

	ULL powers[11];
	for(int i = 0; i < 11; i++) powers[i] = pow(i, N - 1);

	vector<ULL> coinjams;
	vector<vector<ULL> > divisors;

	vector<ULL> numbers;
	for(int i = 0; i < 9; i++) numbers.push_back(powers[i + 2] + 1);

	for(int counter = 0; counter < maxx; counter++)
	{
		if(coinjams.size() == J) break;

		string numberBits = "00000000000000";
		int bit = 13;
		int myCounter = counter;
		while(counter > 0)
		{
			numberBits[bit--] = (counter % 2) + '0';
			counter /= 2;
		}
		counter = myCounter;

		for(int i = 0; i < 9; i++)
		{
			int base = i + 2;
			numbers[i] = powers[base] + 1;

			ULL addition = 0;
			for(int j = 0; j < 14; j++)
			{
				addition *= base;
				addition += (numberBits[j] - '0');
			}

			numbers[i] += addition * base;
		}

		vector<ULL> currentDivisors;
		for(int i = 0; i < 9; i++)
		{
			int base = i + 2;
			ULL number = numbers[i];

			bool found = false;
			ULL squareroot = sqrt(number);
			for(ULL j = 2; j <= squareroot; j++)
			{
				if(number % j == 0)
				{
					found = true;
					currentDivisors.push_back(j);
					break;
				}
			}

			if(!found) break;
		}

		if(currentDivisors.size() == 9)
		{
			divisors.push_back(currentDivisors);
			coinjams.push_back(counter);
			//cout << "YAY " << coinjams.size() << " / " << counter << endl;
		}
	}


	cout << "Case #1:" << endl;
	for(int i = 0; i < J; i++)
	{
		cout << make_coinjam(coinjams[i]) << " ";
		for(int j = 0; j < 8; j++) cout << divisors[i][j] << " ";
		cout << divisors[i][8] << endl;
	}


	return 0;
}

string make_coinjam(int coinjam)
{
	string s = "1000000000000001";
	for(int i = 14; i > 0; i--)
	{
		if(coinjam % 2 == 1) s[i] = '1';
		coinjam /= 2;
	}

	return s;
}