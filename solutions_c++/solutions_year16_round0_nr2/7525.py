#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

void main()
{
	ifstream ifs("Resources/input.in", std::ifstream::in);
	unsigned int samples;
	ofstream ofs("Resources/output.txt", std::ofstream::out);
	
	ifs>>samples;
	for(int i=1;i<=samples;i++)
	{
		string stack;
		ifs>>stack;
		
		//Represent the stack reading left to right as bottom to top
		std::reverse( stack.begin(), stack.end());

		//Our goal now is simple: Keep playing with this binary's digits until it's 0
		unsigned int steps = 0;
		for(unsigned int i=0; i<stack.length(); i++)
		{
			if( (stack[i] == '-' && !(steps%2) ) || (stack[i] == '+' && (steps%2) ) )
			{
				steps++;
			}
		}

		ofs<<"Case #"<<i<<": "<<steps<<"\r\n";
	}
}