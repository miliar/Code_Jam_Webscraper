// gcjA.cpp
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream infile("input.in");
	ofstream OF("output.txt");

	int T;
	infile >> T;

	for (int i = 0; i < T; i++) {

		string buf;
		infile >> buf;

		int Nflips = unique(buf.begin(), buf.end()) - buf.begin() -( (buf.back() == '+')?1:0);

		OF << "case #" << i + 1 << ": " << Nflips << endl;
	}

	return 0;
}
