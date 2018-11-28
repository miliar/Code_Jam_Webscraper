#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <iostream>
using namespace std;

bool IsPalindrome(int n)
{
	stringstream stream;
	stream << n;
	string number = stream.str();
	for(unsigned int i = 0 ; i < number.size()/2 ; ++i)
	{
		if(number[i] != number[number.size()-i-1])
			return false;
	}

	return true;
}

bool IsOk(int c)
{
	if(!IsPalindrome(c)) return false;

	double r = sqrt(c);
	if(r != floor(r)) return false;

	if(!IsPalindrome((int)r)) return false;

	return true;
}

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	int T;
	input >> T;

	for(int i = 1 ; i <= T ; ++i)
	{
		int count = 0;

		int min, max;
		input >> min >> max;

		for(int c = min ; c <= max ; ++c)
		{
			if(IsOk(c))
				++count;
		}

		output << "Case #" << i << ": " << count;
		if(i+1 <= T)
			output << endl;
	}

	input.close();
	output.close();
}