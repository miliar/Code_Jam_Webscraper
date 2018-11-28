#include<fstream>
#include<string>
#include<sstream>
#include<iostream>
#include<math.h>
#include<iomanip>
#include<map>
using namespace std;
int main ()

{
	string ifile = "input.txt", ofile = "output.txt";
	ifstream input;
	input.open(ifile);
	stringstream ss;
	int cases;
	int s;
	string sequence;
	input>>cases;
	for(int c = 1; c <= cases; ++c)
	{
		input>>s;
		input>>sequence;
		long friends=0,standing=0;
		char tmp;
		int p;
		for(int level = 0; level <= s; ++level)
		{
			tmp = sequence[level];
			p = tmp - '0';
			if(standing >= level)
			{
				standing += p;
			}
			else
			{
				int nfriends = (level - standing);
				standing +=(nfriends + p);
				friends += nfriends;
			}
		}
		ss<<"Case #"<<c<<": " << friends<< "\n";
	}
	input.close();
	ofstream output;
	output.open(ofile);
	output<<ss.rdbuf();
	output.flush();
	output.close();
	return 0;
}