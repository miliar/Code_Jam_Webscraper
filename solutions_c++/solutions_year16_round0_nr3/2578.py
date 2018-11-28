#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;
typedef long long LL;

#define N 16
#define J 50

int main() {
	FILE *fin = freopen("C-small.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("C-small.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": " << endl;

		//int n,j;
		//cin >> n >> j;

		unordered_set<unsigned long long> numbersSet; // holds number in base 10
		int counter = 0;

		while (counter < J)
		{
			int digits[N];
			digits[0] = 1;
			digits[N - 1] = 1;
			
			for (int i = 0; i < N - 2; i++)
			{
				digits[i+1] = rand() % 2;
			}

			unsigned long long current = digits[0];
			int base = 10;
			
			for (int i = 1; i < N; i++)
			{
				current *= base;
				current += digits[i];
			}
			
			if (numbersSet.find(current) != numbersSet.end()) // found
			{
				continue;
			}

			numbersSet.insert(current);
			int divisors[9] = { -1, -1, -1, -1, -1, -1, -1, -1, -1 };

			for (int base = 2; base < 11; base++)
			{
				unsigned long long temp = digits[0];

				for (int i = 1; i < N; i++)
				{
					temp *= base;
					temp += digits[i];
				}

				for (int i = 2; i < temp-1; i++)
				{
					if (temp % i == 0)
					{
						divisors[base - 2] = i;
						break;
					}
				}

				if (divisors[base - 2] == -1)
				{
					// not found - invalid number
					break;
				}
			}

			bool invalidNumber = false;
			for (int i = 0; i < 9; i++)
			{
				if (divisors[i] == -1)
				{
					invalidNumber = true;
					break;
				}
			}

			if (!invalidNumber)
			{
				for (int i = 0; i < N; i++)
				{
					cout << digits[i];
				}

				for (int i = 0; i < 9; i++)
				{
					cout << " " << divisors[i];
				}

				cout << endl;

				counter++;
			}
		}
	}

	return 0;
}