#include <iostream>
#include <math.h>
#include<sstream>
#include <string>


bool isPalindrome(long long x)
{
	std::stringstream ss;
	ss<<x;
	std::string num = ss.str();

	for(int i=0; i<num.size()/2; i++)
	{
		if(num[i] != num[num.size()-1 - i])
			return false;
	}

	return true;
}

bool isInRange(long long a, long long b, long long x)
{
	return x >= a && x <=b;
}

long long sqrtll(long long x)
{
	return sqrt(static_cast<long double>(x));
}

long long countFairSqare(long long  a, long long b)
{
	long long count = 0;
	long long start = sqrtll(a);
	long long end =  sqrtll(b) + 1;

	for(long long i = start; i<end; i++)
	{
		if(isInRange(a, b, i*i) && isPalindrome(i) && isPalindrome(i*i)) count++;
	}
	return count;
}

int main()
{
	int count;
	long long a, b;
	std::cin>>count;

	for(int i=0; i<count; i++)
	{
		std::cin>>a>>b;

		std::cout<<"Case #"<<i+1<<": "<<countFairSqare(a,b)<<"\n";
	}
	return 0;
}