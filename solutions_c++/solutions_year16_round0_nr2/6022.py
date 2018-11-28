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

bool isSad(std::vector<char> input)
{
	for(auto ch : input)
		if(ch=='-')
			return true;
	return false;
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
		std::vector<char> pancakesStack;
		std::stringstream lineStream(line) ;
		for (int i = line.size()-1; i >= 0; --i)
			pancakesStack.push_back(line[i]);

		int totalFlipsPerformed = 0;
		while(isSad(pancakesStack))
		{
			int countToFlip = 0;
			char topType = pancakesStack.back();
			pancakesStack.pop_back();
			countToFlip++;
			while(pancakesStack.size()>0 && pancakesStack.back() == topType)
			{
				countToFlip++;
				pancakesStack.pop_back();
			}
			char toAdd = (topType == '+') ? '-' : '+' ;
			for(int j=0;j<countToFlip;++j)
				pancakesStack.push_back(toAdd);
			totalFlipsPerformed++;
		}

		std::cout << totalFlipsPerformed << "\n";
	}
}
