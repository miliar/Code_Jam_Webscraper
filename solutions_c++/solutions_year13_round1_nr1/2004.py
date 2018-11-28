#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;


int main()
{
	ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");

	//ifstream in("A-large.in");
    //ofstream out("A-large.out");

	int iTasks;
	in >> iTasks;


	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		unsigned __int64 r, t;
		in >> r >> t;
		r++;

		__int64 nCircles = 0;
		while( t >= 2 * r - 1 )
		{
			t -= 2 * r - 1;
			r += 2;
			nCircles++;
		}
		out << "Case #" << iCount << ": " << nCircles;
		out << endl;
	}
	return 0;
}
