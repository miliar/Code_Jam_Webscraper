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
	//ifstream in("A-small-attempt0.in");
	//ofstream out("A-small-attempt0.out");

	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int R, C, W;
		in >> R >> C >> W;
		int odd = C % W == 0 ? 1 : 0;
		int result = (C / W) * R + W - odd;

		out << "Case #" << iCount << ": " << result << endl;
	}
	return 0;
}
