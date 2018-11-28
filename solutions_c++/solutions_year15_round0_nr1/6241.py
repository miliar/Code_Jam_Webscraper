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
	ifstream input ("A-large.in");
	
	int tests, test = 1, mS, friends = 0, standing = 0;
	string in;
	vector<int> shynessLevels;

	input >> tests;
	while( tests-- )
	{
		input >> mS >> in;
		for (int i = 0; i < mS+1; i++)
		{
			shynessLevels.push_back( int( in[i] ) - 48 );
		}

		for (int i = 0; i < shynessLevels.size(); i++)
		{
			standing += shynessLevels[i];
			if( standing <= i )
			{
				standing++;
				friends++;
			}
		}

		output << "Case #" << test++ << ": " << friends;
		if( tests != 0 )
		{
			output << endl;
		}

		shynessLevels.clear();
		friends = 0;
		standing = 0;
	}

	input.close();
	output.close();
	return 0;
}