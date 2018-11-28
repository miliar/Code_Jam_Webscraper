#include <algorithm>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
	
	int T, X, R, C, t, done, d;
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");

	fin >> T;
	t=0;
	while(++t <=T)
	{
		fin >> X >> R >> C;
		done = false;			// GABRIEL
		if (X == 1)
		{
			// always GABRIEL
		}
		else if(X == 2)
		{
			d = R*C;
			if (d==1||d==3||d==9) done = true;
		}
		else if(X == 3)
		{
			d = R*C;
			if (d==1||d==2||d==3||d==4||d==8||d==16) done = true;
		}
		else
		{
			d = R*C;
			if (d==1||d==2||d==3||d==4||d==6||d==8||d==9) done = true;
		}
		if (done)
			fout << "Case #" << t << ": RICHARD\n";
		else fout << "Case #" << t << ": GABRIEL\n";
	}
	fin.close();
	fout.close();
	return 0;
}