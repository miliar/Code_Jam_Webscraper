// reading a text file
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

unsigned long long int* divisor = new unsigned long long int[9];
unsigned long long int* bNumbers = new unsigned long long int[9];

int isPrime(unsigned long long int d)
{
	long int m = ceil(sqrt(d));
	
	// cout << m << endl;
	
	for(int i = 2; i < m + 1; i++)
	{
		if((d % i) == 0)
			return 0;
	}
	return 1;
}

int isCoin(unsigned long long int num, int length)
{
	for(int i = 0; i < 9; i++)
		bNumbers[i] = 0;
	
	// int n = num;
	int len = 0;
	
	while(len < length)
	{
		int bit = ((num >> (len)) & 1);
		// int bit = num[len];
		// cout << ((num >> 1));
		// cout << ((num >> (length - len - 1)) & 1);
		
		if(bit)
		{
			for(int i = 0; i < 9; i++)
				bNumbers[i] = bNumbers[i] + pow(i + 2, len);
			// cout << len << endl;
		}

		len++;
	}
	
	// for(int i = 0; i < 9; i++)
		// cout  << bNumbers[i] << endl;
	
	for(int i = 0; i < 9; i++)
	{
		if(isPrime(bNumbers[i]))
		{
			// cout << "fsfsd";
			return 0;
		}
					
	}
	
	return 1;
}

int main () {
	// define variables
	int numTC;
	int N, J;

	ifstream myfile ("C-small.in");
	ofstream savefile ("C-small.out");
	
	if(!myfile.is_open())
		cout << "File not found";

	myfile >> numTC;

	for(int t = 0; t < numTC; t++) // run each test case
	{	
		myfile >> N;
		myfile >> J;
		
		// int h = 2147483647*2;
		
		// cout << ((h >> 32) & 11111111111111111111111111111111);
		// cout << ((h >> 31) & 11111111111111111111111111111111);
		// cout << h;
		
		// cout << isPrime(9);
		
		// cout << isCoin(9, 4);
		
		// if(isCoin(9, 4))
		// {
			// for(int i = 0; i < )
		// }
		
		// cout << ((n >> 4) & 4);
		// cout << (n >> 2) & 1;
		// cout << (n >> 3) & 1;
		// cout << (n >> 4) & 1;
		
		int count = 0;
		
		
		// int N = 32;
		// int J = 50;
		
		savefile << "Case #" << (t + 1) << ": " << endl;
		for(unsigned int n = (unsigned int)pow(2, N-1) + 1; n <= (unsigned int)pow(2, N) - 1; n = n + 2 )
		{
			// cout << pow(2, N-1) + 1 << endl;
		// int n = 6;
			if(isCoin(n, N))
			{
				// cout << ((n >> N) & 1111111111111111) << endl;
				savefile << bNumbers[8] << " ";
				
				for(int b = 0; b < 9; b++)
				{
					unsigned long long int m = ceil(sqrt(bNumbers[b]));
					for(unsigned long long int i = 2; i < m + 1; i++)
					{
						if((bNumbers[b] % i) == 0)
						{
							savefile << i << " ";
							break;
						}
							
					}
				}
				count++;
				savefile << endl;
			}
			if(count == J)
				break;
		}
		
		// cout << isPrime(101) << endl;
	}

	myfile.close();
	savefile.close();

	return 0;
}


