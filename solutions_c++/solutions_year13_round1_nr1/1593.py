#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include "number.cpp"
#include <math.h>
using namespace std;


int main()
{
	//open file
	char inFileName[10] = "small.in";
	char outFileName[10] = "small.out";
	ifstream f1;
	f1.open(inFileName, ios::in);	
	ofstream f2;
	f2.open(outFileName, ios::out);

	//process
	int T;
	f1 >> T;
	for(int c = 0;c < T;++c)
	{
		//read data
		//number r, t;
		int r, t;
		f1 >> r;
		f1 >> t;
		int k = (1 - 2*r+sqrt(4*r*r-4*r+1+8*t)) / 4;

		f2 << "Case #" << c+1 << ": " << k << endl;
    }
	f1.close();
	f2.close();
    return 0;

}
