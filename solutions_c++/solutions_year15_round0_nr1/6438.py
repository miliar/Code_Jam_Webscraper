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
	int Smax = 0;
	int standup = 0;
	char input;
	int next = 0;
	int need = 0;

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
	need = 0;
	
	infile>>Smax;
	//cout<<Smax<<endl;
	infile>>input;
	//cout<<(int)input<<endl;
	standup = (int)input - 48;
	for (int j = 1; j < Smax+1; ++j)
	{
		infile>>input;
		next = (int)input-48;
		if (standup>=Smax)
		{//do not need ppl anymore, finish scan
		}
		else if (j<=standup)
		{
			standup += next;
		}
		else
		{
			need++;
			standup = j+next;
		}
	}




	outfile<<"Case #"<<i<<": "<<need<<endl;
}






}