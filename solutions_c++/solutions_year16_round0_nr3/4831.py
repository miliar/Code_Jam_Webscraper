#include <iostream>
#include <algorithm>
#include <regex>
#include <sstream>
#include <streambuf>
#include <fstream>
#include <iomanip>
#include <math.h>
//______________________________________________________________________
#include <vector>			// dynamic array.

#include <string>
#include <unordered_map> 	// hash tables.
#include <unordered_set>	// unordered_multiset.
#include <array>
#include <bitset> 			// bit array
#include <deque> 			// double-ended queue.
#include <vector>			// dynamic array.
#include <forward_list> 	// singly linked list
#include <list>				// doubly linked list.
#include <map>				// sorted associative array and multimap.
#include <queue>			// priority queue.
#include <set>				//sorted associative containers or sets.
#include <stack>
//______________________________________________________________________
#include <sstream>
#include <exception>
#include <stdexcept>
//______________________________________________________________________
std::string intToString (int a)
{
    std::ostringstream temp;
    temp<<a;
    return temp.str();
}
double stringToDouble (std::string word)
{
	return atof(word.c_str());
}
double stringToInt (std::string word)
{
	return atoi(word.c_str());
}

bool isPrime(unsigned long long n)
{
	if(n==1)
		return false;
	else if( n<4 )
		return true;
	else if (n%2==0)
		return false;
	else if (n<9)
		return true ;
	else if (n%3==0)
		return false;
	else
	{
		int factor=5;
		int r = floor( sqrt(n*1.0) );
		while( factor<=r )
		{
			if ( n%factor==0 )
				return false;
			factor+=2;
		}
		return true;
	}
}
int getNonTrivDiv(unsigned long long num)
{
	for (unsigned long long  i = 2; i <= sqrt(num); ++i){
		if (num % i == 0)
			return i ;
	}
	return 0;
}
std::string printBitSet(std::bitset<32> input)
{
	std::string mystring =
			input.to_string<char,std::string::traits_type,std::string::allocator_type>();
	int count = 0 ;
	while(mystring[count++] == '0');
	std::string output = mystring.substr(count-1, mystring.size());
	return output;
}
int main()
{
	std::string line, outLine;
	int N,J,jamcoinCount=0;
	bool stop = false;
	std::cout << "Case #1:\n" ;
	//===============
	getline(std::cin, line); // Just skipping the count number
	std::getline(std::cin, line);
	std::stringstream lineStream(line) ;
	lineStream >> N >> J ;
	//===============
	//N=32;J=3;
	//===============
	unsigned long long upperBound = pow(2,N)-1;
	unsigned long long upperBoundBit = pow(2,N-1);

	for(unsigned long long i=0;i<upperBound;++i)
	{
		if(( (i&1) == 0)||( (i&upperBoundBit) == 0))
			continue;
		stop = false;
		std::bitset<32> binaryNum(i);
		outLine = printBitSet(binaryNum);
		outLine += " " ;
		for(int base=2;base<=10;++base)
		{
			unsigned long long num = i , sum=0;
			for(int count=0;count<N;++count)
				if((num & (1 << count)))
					sum+= pow(base,count);
			if(isPrime(sum) == false)
			{
				int div = getNonTrivDiv(sum) ;
				if(div)
				{
					outLine += intToString(div);
					outLine += " " ;
				}
				else
				{
					stop=true;
					break;
				}
			}
			else
			{
				stop=true;
				break;
			}
		}
		if(stop)
			continue;
		std::cout << outLine <<std::endl;
		jamcoinCount++;
		if(jamcoinCount == J)
			break;
	}
}
