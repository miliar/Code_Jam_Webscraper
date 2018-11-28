/*
https://code.google.com/codejam/contest/6254486/dashboard#s=p2
*/

#include<iostream>
#include<fstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

/*
string getSieve()
{
	long long int small = 32769;
	long long int large = 1111111111111111;

	vector<bool> isPrime((large - 3)/2 + 1, true);
	long long int root = sqrt(large);

	for (long long int i = 3; i <= root; i += 2)
	{
		if (!isPrime[(i - 3)/2])
		{
			continue;
		}

		for (long long int j = i; j <= large; j += 2*i)
		{
			isPrime[(j - 3)/2] = false;
		}
	}
	
	//vector<bool> isPrime((large - small)/2 + 1, true);
	string result = "";
	for (long long int i = small; i <= large; i += 2)
	{
		cout << isPrime[(i - 3)/2] << " ";
		result += isPrime[(i - 3)/2] ? "1" : "0";

		////string divisor = "-1";
		////if (!isPrime[(i - 3)/2])
		////{
		////	for (long long int j = 3; j <= root; j += 2)
		////	{
		////		if (i % j == 0)
		////		{
		////			divisor = to_string(j);
		////			break;
		////		}
		////	}
		////}

		////result += divisor + " ";
	}

	cout << endl << endl;

	return result;
}
*/

long long int convertBaseAndCheckPrimality(
	long long int val,
	int base,
	vector<vector<long long int>> &powers,
	vector<long long int> &primes)
{
	long long int n = 0;

	int index = 0;
	while (val)
	{
		int digit = val % 10;
		if (digit)
		{
			//n += powers[(base/2) - 1][digit];
			n += pow(base, index);
		}

		val /= 10;
		index++;
	}

	for (int i = 0; i < primes.size(); i++)
	{
		if (n % primes[i] == 0)
		{
			return primes[i];
		}
	}

	return 0;
}

bool printResult(
	long long int val,
	vector<vector<long long int>> &powers,
	vector<long long int> &primes)
{
	int isJam = true;
	vector<int> divisors(11, 2);
	for (int base = 2; base <= 10; base += 2)
	{
		int divisor = convertBaseAndCheckPrimality(val, base, powers, primes);
		if (!divisor)
		{
			isJam = false;
			break;
		}

		divisors[base] = divisor;
	}

	if (isJam)
	{
		cout << val << " ";

		for (int i = 2; i <= 10; i++)
		{
			cout << divisors[i] << " ";
		}

		cout << endl;
	}

	return isJam;
}

int main() {
	/*ifstream cin;
	ofstream cout;
	cin.open("coinjam.in");
	cout.open("coinjam.out");*/

	//string result = getSieve();
	//cout << result;

	long long int arr1[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 };
	long long int arr[][sizeof(arr1)/sizeof(*arr1)] = {
		{ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 },
		{ 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1.04858e+006, 4.1943e+006, 1.67772e+007, 6.71089e+007, 2.68435e+008, 1.07374e+009 },
		{ 1, 6, 36, 216, 1296, 7776, 46656, 279936, 1.67962e+006, 1.00777e+007, 6.04662e+007, 3.62797e+008, 2.17678e+009, 1.30607e+010, 7.83642e+010, 4.70185e+011 },
		{ 1, 8, 64, 512, 4096, 32768, 262144, 2.09715e+006, 1.67772e+007, 1.34218e+008, 1.07374e+009, 8.58993e+009, 6.87195e+010, 5.49756e+011, 4.39805e+012, 3.51844e+013 }
	};

	int cols = sizeof(arr1)/sizeof(*arr1);
	int rows = sizeof(arr)/sizeof(*arr);
	vector<vector<long long int>> powers(rows, vector<long long int>(cols));
	for (int i = 0; i < rows; i++)
	{
		powers[i].assign(arr[i], arr[i] + cols);
	}

	long long int arrPrimes[] = { 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 };
	vector<long long int> primes(arrPrimes, arrPrimes + sizeof(arrPrimes)/sizeof(*arrPrimes));

    long long int testCases;
	cin >> testCases;

	long long int tc = 0;
    while (++tc <= testCases)
    {
		cout << "Case #" << tc << ":" << endl;

        int n, jams;
		cin >> n >> jams;

		string str = "1000000000000001";

		int count = 0;

		count += printResult(stoll(str), powers, primes);

		for (int i = 14; i > 1; i--)
		{
			str[i] = '1';

			for (int j = i - 1; j >= 1; j--)
			{
				str[j] = '1';
				count += printResult(stoll(str), powers, primes);
				str[j] = '0';

				if (count == jams)
				{
					break;
				}
			}

			str[i] = '0';

			if (count == jams)
			{
				break;
			}
		}
    }

	/*cin.close();
	cout.close();*/
    
    return 0;
}
