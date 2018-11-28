#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	
	input.open("B-large.in");
	output.open("output.txt");
	
	int T, S, y;
	string stack;
	char current;
	input >> T;
	
	for(int t = 1; t <= T; t++)
	{
		output << "Case #" << t << ": ";
		input >> stack;
		S = stack.length();
		y = 0;
		current = stack[0];
		for(int s = 1; s < S; s++)
		{
			if(current != stack[s])
			{
				y++;
				current = stack[s];
			}
		}
		if(current == '-')
		{
			y++;
		}
		output << y << endl;
	}
	
	input.close();
	output.close();
	
	return 0;
}
