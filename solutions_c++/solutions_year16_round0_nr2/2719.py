#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    //ifstream in("small-practice.in");
    ifstream in("B-large.in");
    ofstream out("output.out");

    unsigned int T;
    in >> T;

    for( unsigned int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";

		string s;
		in >> s;

		char currentChar = s.at(0);
		unsigned int changes = 0;

		for( unsigned int iter = 1; iter < s.length(); iter++ )
		{
			if( s.at(iter) != currentChar )
			{
				currentChar = s.at(iter);
				changes++;
			}
		}
		if( s.at( s.length()-1 ) == '-' ) changes++;

        out << changes << endl;
    }

    return 0;
}
