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

int main()
{
	std::string line, token, outLine;

	int caseCounter=1;
	getline(std::cin, line); // Just skipping the count number
	while (std::getline(std::cin, line))
	{
		outLine = "Case #" ;
		outLine+= intToString(caseCounter++) ;
		outLine+=": ";
		std::cout << outLine;
		std::stringstream lineStream(line) ;
		int number ;
		lineStream >> number;
		if(number == 0)
			std::cout << "INSOMNIA" << std::endl;
		else
		{
			int originalNumber = number;
			int numberFlags = 0;
			int count=1;
			while(numberFlags!=1023) // 10 bits
			{
				number = originalNumber * count++;
				while(number)
				{
					int unit = number % 10;
					numberFlags |= (0x1 << unit);
					number/=10;
				}
			}
			std::cout << originalNumber * (count-1) << std::endl ;
		}
	}
}
