/*
 * fair_and_square.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Matt
 */

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int is_palindrome(long long n)
{
	int num_digits = (int)log10(n) + 1;

	for(int i=0; i<num_digits/2; i++)
	{
		if((n % (long long)pow((double)10, i+1))/(long long)pow((double)10, i)
				!= (n % (long long)pow((double)10, num_digits-i))/(long long)pow((double)10, num_digits-i-1))
		{
			return 0;
		}
	}

	return 1;
}

int main()
{
	ofstream out;
	out.open("answer.txt");

	int num_cases;
	cin >> num_cases;

	for(int i=1; i<=num_cases; i++)
	{
		long long A, B;
		cin >> A; cin >> B;

		int count = 0;
		for(long long j=A; j<=B; j++)
		{
			if(is_palindrome(j))
			{
				cout << j << endl;
				if(sqrt(j) == (long long)sqrt(j))
				{
					if(is_palindrome((long long)sqrt(j)))
					{
						count++;
					}
				}
			}
		}

		out << "Case #" << i << ": " << count << endl;
	}

	out.close();
}
