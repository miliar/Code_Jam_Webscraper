#include <iostream>
#include <fstream>
#include <bitset>

using namespace std;
bool checkPrime(_int64 sum);

int main()
{
	int J, N = 0;
	int counter = 0;
	int test_cases;
	_int64 sum = 0;
	int prime = 0;
	int answer = 0;
	int divisors[9];


	ifstream fin;
	fin.open("C.txt");
	fin >> test_cases;
	ofstream fout;
	fout.open("bitjam.txt");
	
	while (counter < test_cases)
	{
		int * jamcoin;

		fin >> N >> J;
		counter++;
		int index = 1;
		answer = 0;
		jamcoin = new int[N];
		jamcoin[0] = 1;
		jamcoin[N - 1] = 1;
		fout << "Case #" << counter << ":" << endl;

		for (int k = 0; k < pow(2, N - 2); k++)//loop 2^J possible inputs
		{
			index = 1;
			bitset<32> bin = k;//A will hold the binary representation of N 
			for (int i = 0, j = N - 2; i < N - 2; i++, j--)
			{
				jamcoin[index] = bin[i];
				index++;
			}
			for (int l = 0; l < 9; l++)
				divisors[l] = 0;
			for (int i = 10; i >=2; i--)
			{
				prime = 0;
				sum = 0;
				for (int j = 0; j <N; j++)
				{
					sum = sum + (jamcoin[N-1-j] * pow(i, j));
				}
				
				if (checkPrime(sum) == true)
				{
					prime++;
					break;
				}
				else
					for (int l = 2; l<(sum / 2) + 1; l++)
					{
						if (sum%l == 0)
						{
							divisors[i - 2] = l;
							break;
						}
					}
			}
			if (prime == 0)
			{
				answer++;
				for (int i = 0; i < N; i++)
					fout << jamcoin[i];
				for (int l = 0; l < 9; l++)
				fout << "  " << divisors[l];
			fout << endl;

			}
			
			if (answer == J)
				break;
		}
		delete[] jamcoin;
	}

	return 0;
}

bool checkPrime(_int64 sum)
{
	if (sum == 2)
		return false;

	for (int i = 2; i <= sqrt(sum ); i++)
	{
		if (sum%i == 0)
			return false;
	}
	return true;

}