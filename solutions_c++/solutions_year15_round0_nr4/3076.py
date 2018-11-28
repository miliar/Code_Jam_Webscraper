#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
	ofstream output; output.open( "output.txt" );
	ifstream input ("D-small-attempt0.in");

	int tests, test = 1, x ,r, c;
	string answer = "GABRIEL";

	input >> tests;
	while( tests-- )
	{
		input >> x >> r >> c;
		if( x > 7 )
		{
			answer = "RICHARD";
		}
		else if( ( r * c ) % x != 0 )
		{
			answer = "RICHARD";
		}
		else if( ( x == 3 || x == 4 ) && ( r == 1 || c == 1 ) )
		{
			answer = "RICHARD";
		}
		else if( x == 4 && ( r * c == 8 ) )
		{
			answer = "RICHARD";
		}
		else if( x == 4 && r == 2 && c == 2 )
		{
			answer = "RICHARD";
		}
	
		output << "Case #" << test++ << ": " << answer;
		if( tests != 0 )
		{
			output << endl;
		}
		answer = "GABRIEL";
	}

	input.close();
	output.close();
	return 0;
}