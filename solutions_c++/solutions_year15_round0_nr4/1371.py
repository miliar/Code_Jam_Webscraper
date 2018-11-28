#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <functional>
#include <algorithm>
#include <cmath>
using namespace std;

int t, x, r, c;

int main()
{
	//ifstream infile("D-large.in");
	ifstream infile("D-small-attempt3.in");
	//ifstream infile("in.txt");
    ofstream outfile;
    outfile.open("out.txt");
	infile >> t;
	for (int i = 1; i <= t; i++)
	{
		infile >> x >> r >> c;
		if(x>=7)
			outfile << "Case #" << i << ": " << "RICHARD" << endl;
		else if((r*c)%x!=0)
			outfile << "Case #" << i << ": " << "RICHARD" << endl;
		else if((x > r)&&(x > c))
			outfile << "Case #" << i << ": "<< "RICHARD" << endl;
		else if(( (x-1)/2+1 > r)||( (x-1)/2+1 > c))
			outfile << "Case #" << i << ": " << "RICHARD" << endl;
		else if( (( (x-1)/2+1 >= r)||( (x-1)/2+1 >= c)) && (x>3) )
			outfile << "Case #" << i << ": " << "RICHARD" << endl;
		else
			outfile << "Case #" << i << ": " << "GABRIEL" << endl;
	}
}