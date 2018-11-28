#include <iostream>
#include <set>
#include <string>
#include <cmath>
#include <vector>
#include <bitset>
using namespace std;

typedef unsigned long long ull;

ull isPrime(ull x)
{
	for (ull i = 2; i < sqrt(x); i++)
		if (x % i == 0)
		{
		//	std::cout << " returning new " << i << std::endl;
			return i;
		}
	//std::cout << "Returning orignal." << std::endl;
	return x;
}

#define MAX 15

int main()
{
	std::vector< ull > results;
	std::cout << "Case #1:" << std::endl;
	
	for (ull i = 0; i < 1 << MAX; i++)
	{
		//std::cout << "Testing: " << i;
		ull x = i; 
		
		x <<= 1;
		x += 1 << MAX;
		x += 1;
		ull y = x;
		//std::cout << " Value: " << x << std::endl;
			 
		ull b[9] = { 0,0,0,0,0,0,0,0,0 };

		int counter = 0;
		while (x != 0)
		{
			if (x % 2)
			{
				for (int j = 0; j < 9; j++)
					b[j] += pow(j + 2, counter);
			}

			x /= 2;
			++counter;
		}

		ull a[9] = { 0,0,0,0,0,0,0,0,0 };
		bool result = true;
		

		for (int j = 0; j < 9; j++)
		{
			a[j] = isPrime(b[j]);
			if (a[j] == b[j])
			{
				result = false;
				break;
			}
		}
		/*
		std::cout << "Values: " << std::endl;
		for (int j = 0; j < 9; j++)
		{
			std::cout << b[j] << " ";
		}
		std::cout << std::endl;
		std::cout << "Divisors" << std::endl;
		for (int j = 0; j < 9; j++)
		{
			std::cout << a[j] << " ";
		}
		std::cout << std::endl;
		*/

		if (result)
		{

			std::bitset<MAX + 1> bit;
			counter = 0;
			while (y != 0)
			{
				if (y % 2)
				{					
					bit[counter] = 1;
				}
				else
				{
					bit[counter] = 0;
				}
				
				y /= 2;
				++counter;
			}
			std::cout << bit;
			std::cout << " ";
			for (int j = 0; j < 9; j++)
			{
				std::cout << a[j] << " ";
			}
			std::cout << std::endl;
			results.push_back(y);
			if (results.size() == 50)
				cin.get();

		}
		else
		{
			//std::cout << i << " failed." << std::endl;
		}
		//std::cin.get();
	}



	std::cin.get();
}