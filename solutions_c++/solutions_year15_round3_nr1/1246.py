//name Yufei Wang

#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <iomanip>
#include <math.h>
#include <algorithm>
using namespace std;

int main (int arg, char* argv[])
{
	int T = 0;
	int R = 0;
	int C = 0;
	int W = 0;
	//string input;

	bool success;

	string filename;
	ifstream infile;
	ofstream outfile;
	infile.open(argv[1], ios::in);
	outfile.open("result.txt", ios::out);
	if(!infile)
	 {
	  cout <<" cannot open file" ;
	  exit(0);
	  }

	infile >> T;


	int missrow, hitrow, remain, total;
	for (int i = 1; i <= T; ++i)
	{	

		
		infile>>R;
		//cout<<Smax<<endl;
		infile>>C;
		infile>>W;

		missrow = C/W;
		hitrow = 0;
		remain = C - (C/W)*W;

		if(remain == 0)
		hitrow = (C/W)-1 +W;
		else
		hitrow = (C/W) + W;

		total = hitrow + (R-1)*missrow;

	//	cout<<input<<endl;

			outfile<<"Case #"<<i<<": "<<total<<endl;
	}






}