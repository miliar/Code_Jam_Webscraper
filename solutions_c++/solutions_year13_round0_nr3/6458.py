#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <sstream>

bool isPalindrom(const std::string& num)
{
	int len = num.length();

	if(len <2)
		return true;
	else if(len == 2)
		return num[0] == num[1];
	else
	{
		for(short i = 0;i<(int)(len/2);++i)
		{
			if(num[i] != num[len-i-1])
				return false;
		}
	}

	return true;
}

bool isFairSquare(const long& num)
{
	double result = sqrt((double)num);
	std::stringstream number,square_root_num;

	long firstDecimalPlace = (long)((result-(long)result)*10);
	
	if(firstDecimalPlace != 0) //Not Perfect Square
		return false;

	number.clear();
	square_root_num.clear();

	number<<num;
	square_root_num<<(long)result;

	//sprintf(square_root,"%ld",square_root_num);
	return (isPalindrom(number.str()) && isPalindrom(square_root_num.str()));
}

long FairSquareCount(const long& first,const long& sec)
{
	long count = 0;

	for(long i = first;i<= sec;++i)
	{
		if(isFairSquare(i))
			++count;
	}

	return count;
}

int main(void)
{
	short T;
	long first,sec;

	std::cin>>T;
	for(short i = 1;i<=T;++i)
	{
		std::cin>>first>>sec;
		std::cout<<"Case #"<<i<<": "<<FairSquareCount(first,sec)<<std::endl;
	}
	//system("pause");
	return 0;
}
