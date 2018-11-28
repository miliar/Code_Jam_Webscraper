#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
  	freopen("A-large.out", "w", stdout);
	int cases, number, copynumber, mult = 1, numdigits, currentdigit, done = 0;
	vector <int> digits(10, 0);
	cin >> cases;
	for(int i = 0; i < cases; i++)
	{
		cin >> number;
		done = 0;
		mult = 1;
		for(int n = 0; n < 10; n++)
		{
			digits[n] = 0;
		}
		while(mult < 100 && done == 0)
		{
			copynumber = number * mult;
			numdigits = 0;
			while(copynumber >= 1)
			{
				copynumber /= 10;
				numdigits++;
			}
			for(int z = 1; z <= numdigits; z++)
			{
				currentdigit = ((number * mult) / pow(10, z - 1));
				currentdigit %= 10;
				digits[currentdigit] = 1; 
			}
			done = 1;
			for(int w = 0; w < 10; w++)
			{
				if(digits[w] == 0)
				{
					done = 0;
				}
			}
			if(done == 0)
			{
				mult++;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if(done == 0)
		{
			cout << "INSOMNIA" << endl;
		}	
		else
		{
			cout << number * mult << endl;
		}
	}
}

