#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>

#define forl(i,a,b) for(int i = a; i < b; ++i)

using namespace std;

bool isPalindrome(uint64_t num)
{
	char buffer[8192];
	int len = sprintf(buffer, "%llu", num);
	forl(k,0,(len+1 /2))
	{
//		cerr << "comparing (" << k << " , " << len << ") " << buffer[k] << " and " << buffer[len-k-1] << endl;
		if (buffer[k] != buffer[len-k-1])
			return false;
	}
	return true;
}


int main(int argc, char **argv)
{
	int t;
	cin >> t;
	forl(test,1,t+1)
	{
		uint64_t a, b;
		cin >> a >> b;
		uint64_t ra = (uint64_t)sqrt((double)(a)) - 1;
		uint64_t rb = (uint64_t)sqrt((double)(b)) + 3;

		uint64_t numPals = 0;
		//#pragma omp parallel for
		for (uint64_t num = ra; num <= rb; ++num)
		{
			if (num*num < a) continue;
			if (num*num > b) continue;
			if (!isPalindrome(num))
				continue;
			if (!isPalindrome(num*num))
				continue;
//			cerr << "found: " << num << " " << (num*num) << endl;
			numPals++;
		}

		cout << "Case #" << test << ": " << numPals << endl;
	}
	return 0;
}
