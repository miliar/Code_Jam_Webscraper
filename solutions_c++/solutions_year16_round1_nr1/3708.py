
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;

typedef unsigned long long USLONG;
//typedef uint64_t USLONG;

//#define fin cin
//#define fout cout

//int main(int argc, char **argv)
int main()
{
	unsigned int T = 0, N = 0, J = 0,
		i = 0,  j = 0, t = 0;
	
	#ifndef fin
	ifstream fin("Input.txt");
	ofstream fout("Output.txt");
	#endif
	
	fin >> T;

	string sIn, sOut;
	char first, current;
	
	for(t = 0; t < T; t++)
	{
		fin >> sIn;
		first = current = sIn[0];
		for(i = 0; i < sIn.size(); i++)
		{
				current = sIn[i];
				if(current >= first)
				{
					sOut = current + sOut;
					first = current;
				}
				else
				{
					sOut = sOut + current;
				}
		}
		fout << "Case #" << t + 1<< ": " << sOut << "\n";
		sOut.clear();
	}
	return 0;
}
