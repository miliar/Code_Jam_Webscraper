#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <set>
#include <vector>
#include <cmath>

using namespace std;



void main(int argc, char* argv[])
{
	int T;
	string str;
	string::iterator si;
	ifstream ifile;
	
	if(argc<=1)
		ifile.open("../example.in");
	else
		ifile.open(argv[1]);
	if(!ifile.is_open())
	{
		cout << "File not Found! in " << endl; 
		exit(-1);
	}
	
	ifile >> T;
	int r,t;
	int result;
	for(int n=1; n<=T; n++)
	{
		ifile >> r >> t;
		result=0;
		r++;
		do
		{
			int r1 = r-1;
			int ml = r*r - (r1*r1);
			t-= ml;
			if(t>=0)
				result++;
			else
				break;
			r+=2;
		}while(true);

		if(result==0)
			result++;
		cout << "Case #" << n << ": " << result << endl;
	}

	ifile.close();
}