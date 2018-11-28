//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>
#include <boost/lexical_cast.hpp>
#include <string>
#include <bitset>
#include <vector>

#include <cstdlib>
#include <cstring>

using namespace std;
using namespace boost;


string flip(const string & stack, int flip_point)
{
	string top_half = stack.substr(0, flip_point);
	std::reverse(top_half.begin(), top_half.end());
	BOOST_FOREACH(char & c, top_half)
	{
		c = (c=='+')? '-': '+';
	}
	return top_half + stack.substr(flip_point);
}


int main() {

	int T;
	cin >> T;

	BOOST_FOREACH(int t, irange(0, T))
	{
		string stack;

		cin >> stack;


		int stack_bottom = stack.size();
		int flip_count = 0;

		while (stack[stack_bottom - 1] == '+')
		{
			stack_bottom--;
		}

		while (stack_bottom > 0)
		{

			int flip_point = 0;

			if (stack[flip_point] == '+')
			{
				// do an extra flip
				while (stack[flip_point] == '+')
				{
					flip_point += 1;
				}

				stack = flip(stack, flip_point);
				flip_count++;
			}

			stack = flip(stack, stack_bottom);
			flip_count++;



			while (stack[stack_bottom - 1] == '+')
			{
				stack_bottom--;
			}

		}



		string output = lexical_cast<string>(flip_count);

		cout << "Case #" << (t+1) << ": " << output << "\n";
	}

	cout.flush();


	return 0;
}


