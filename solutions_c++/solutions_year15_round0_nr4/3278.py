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
	int X = 0;
	int R = 0;
	int C = 0;
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

for (int i = 1; i <= T; ++i)
{	

	
	infile>>X;
	//cout<<Smax<<endl;
	infile>>R;
	infile>>C;
	//cout<<(int)input<<endl;
	switch(X)
	{
		case 1: success = 1;
			break;
		case 2:
			if (R*C%2 ==0)
				success = 1;
			else
				success = 0;
			break;
		case 3:
			if(R*C==12 || R*C ==6 ||R*C ==9)
				success =1;
			else
				success = 0;
			break;
		case 4:
			if(R*C==12 || R*C ==16 )
				success = 1;
			else
				success = 0;
			break;
	}
	if (success)
	{
		outfile<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
	}
	else
		outfile<<"Case #"<<i<<": "<<"RICHARD"<<endl;
}






}