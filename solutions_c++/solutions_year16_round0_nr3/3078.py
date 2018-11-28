#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdint>

using namespace std;

//0 if prime, a non-trivial divisor else
uint64_t isprime(uint64_t n)
{
	uint64_t e = sqrt(n);
	for(uint64_t i = 2; i < e; ++i)
		if(n % i == 0)
			return i;
	return 0;
}

uint64_t toBase(uint64_t n, int b, int N)
{
	uint64_t a = 1;
	uint64_t sum = 1;
	for (int i = 1; i < N; ++i)
	{
		a *= b;
		if (n&1<<i)
			sum += a;
	}
	return sum;
	
}

int main(int argc, char** argv )
{
	int n;
	std::cin >> n; 
	for(int i = 0; i < n; ++i)   
	{
		std::cout << "Case #"<< std::to_string(i+1) << ":" << endl;
		int N;
		int J;		
		std::cin >> N >> J;
		int c = 0;
		for(uint64_t j = 1 << (N-1); j < 1<<N && c < J; j += 2)
		{
			vector<uint64_t> divs(9);
			int k = 2;
			uint64_t a;
			for (k = 2; k < 11; ++k)
			{
				a = toBase(j, k, N);
				divs[k-2] = isprime(a);
				if( divs[k-2] == (uint64_t) 0)
					break;
			}
			if (k == 11)
			{
				cout << a << " ";
				for(k = 0; k < 9; ++k)
					cout << divs[k] << " ";
				cout << endl;
				c++;
			}
		}		
	}
    return 0;
}
