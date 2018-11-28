#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;


int main(int argc, char** argv)
{
string fName = argv[1];

fstream In((fName+".in").c_str(), ios::in);
fstream Out((fName + ".out").c_str(), ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{
	int ret = 0, a = 0, b= 0, c=0;
	int r;
	In >> r;

	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			In >> b;
			if(r==i+1)
				a |= (1<<b);
		}
	}
	In >> r;

	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			In >> b;
			if(r==i+1)
				c |= (1<<b);
		}
	}

	a = a & c;

	string s;
	if(a==0)
		s = "Volunteer cheated!";
	else if (a & (a-1) )
		s = "Bad magician!";
	else
	{	stringstream t;
		for(int j=1; j<17; j++)
			if((1<<j) & a)
				t << j;
		s = t.str();
	}

	Out << "Case #" << h+1 << ": " << s << endl;

}

In.close();

Out.close();

return 0;

}
 
