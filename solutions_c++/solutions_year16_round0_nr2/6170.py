#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <fstream>
using namespace std;

bool IsPrime(long long number)
{	
	long i;
	for (i = 2; i<sqrt(number); i++)
	{
		if (number % i == 0)
		{
			return false;
		}
	}
	return true;
}
int main()
{
	ofstream output;
	ifstream input;
	input.open("B-large.in");
	output.open("output.in");
	long long t;
	input >> t;
	for (long long i = 0; i < t; i++)
	{
		string stack;
		input >> stack;
		char first = stack[stack.size() - 1];
		long long cr = 1;
		char state = first;
		for (long long k = stack.size() - 1; k >= 0; k--)
		{
			if (stack[k] == state)
			{
				continue;
			}
			else
			{
				cr++;
				if (state == '+') state = '-';
				else state = '+';
			}
		}
		long long o = cr;
		cout << cr << endl;
		if (first == '+')
		{
			o = cr - 1;
		}
		
		output << "Case #" << i+1 << ": " << o<<endl;
		//cout << "Case #" << i << ": " << o << endl;
	}
	return 0;
}
