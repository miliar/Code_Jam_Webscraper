#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <string.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using namespace std;

int main(int argc, char** argv) {
	int casen = 0;
	ifstream ifile;
	ofstream ofile;
	//ifile.open("sample.txt");
	ifile.open("A-small-attempt0.in");
	//ifile.open("A-large.in");
	ofile.open("output.txt");
	ifile >> casen;
	for (int c=0; c<casen; c++)
	{
		long long r; // radius
		long long t; // paint volume
		long long round = 0; // round painted
		ifile >> r;
		ifile >> t;
		cout << r << ", " << t << ": ";
		while (t>0)
		{
			t -= (2*r+1);
			if (t>=0)
			{
				round++;
			}
			r += 2;
		}
		cout << round;
		cout << endl;
		
		//cout << "Case #" << c+1 << ": " << msg << endl;
		ofile << "Case #" << c+1 << ": " << round << endl;
	}
	
	long long l = 1000000000000000000;
	cout << l;
	
	ifile.close();
	ofile.close();
	return 0;
}
