#include <iostream>
#include <string>
#include <math.h>
#include <thread>

using namespace std;

int numFound = 0;

bool isPrime(long int numToCheck)
{
		long int numToCheckSqrt = sqrt(numToCheck);
		if(numToCheck <= 0)
		{
			return false;
		}
		for(long int currCheckedNum = 2; currCheckedNum < numToCheckSqrt; currCheckedNum++)
		{
			if(numToCheck % currCheckedNum == 0)
			{
					numFound = currCheckedNum;
					return false;
			}
		}
		return true;
}

int main()
{
		int numCases;
		string inString;
		cin >> numCases;
		getline(cin, inString);
		for(int i = 0; i < numCases; i++) //loop through the cases
		{
				cout << "Case #" << i + 1 << ":" << endl;
				int numDigits, numPossibilities;
				cin >> numDigits;
				cin >> numPossibilities;
				bool bits[numDigits];
				int divisors[9];
				for(int j = 0; j < numDigits; j++)
				{
						bits[j] = false;
				}
				bits[0] = true;
				bits[numDigits - 1] = true;
				for(int j = 0; j < numPossibilities; j++)
				{
						bool allArePrimes = false;
						while(!allArePrimes)
						{
								allArePrimes = true;
								bool overflow = true;
								for(int k = 1; k < numDigits - 1; k++)
								{
										if(bits[k] && overflow)
										{
											bits[k] = false;
										}
										else if(!bits[k] && overflow)
										{
												bits[k] = true;
												overflow = false;
										}
								}
								for(int base = 2; base <= 10; base++)
								{
										long int myNum = 0;
										for(int bit = 0; bit < numDigits; bit++)
										{
												if(bits[bit])
												{
														myNum += pow(base, bit);
												}
										}
										if(isPrime(myNum))
										{
												allArePrimes = false;
										}
										else
										{
												divisors[base - 2] = numFound;
										}
								}
						}
						for(int l = numDigits - 1; l >= 0; l--)
						{
								cout << (bits[l] ? "1" : "0");
						}
						for(int m = 0; m < 9; m++)
						{
								cout << " " << divisors[m];
						}
						cout << endl;
				}
		}
		return 0;
}
