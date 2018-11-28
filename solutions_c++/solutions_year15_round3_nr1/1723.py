#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

int r, c,w, ret, t;
string s;

int main()
{
	ifstream infile("A-small.in");
    ofstream outfile;
    outfile.open("out.txt");
	infile >> t;
	for (int i = 1; i <= t; i++)
	{
		infile >> r >> c >> w;
		ret = c/w + w;
		if(c%w==0) ret--;
		ret*=r;
		outfile << "Case #" << i << ": " << ret << endl;
	}
}