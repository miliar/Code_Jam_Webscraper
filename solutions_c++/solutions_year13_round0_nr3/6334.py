#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;

bool isfair(int n)
{
	string temp;
	string tempreversed;
	stringstream convert;
	convert << n;
	temp = convert.str();
	for(int k = 0; k < temp.length(); k++)
	{
		tempreversed += temp[temp.length() -1 - k];
	}
	if(tempreversed == temp)
	{
	return true;		
	}
return false;
}
int main(int argc, char *argv[]) {
	ofstream outputfile;
 	ifstream inputfile;
 	inputfile.open(argv[1], ios::in);
	outputfile.open("c.out", ios::out);
	int numcases = 0;
	inputfile >> numcases;
	for(int i = 0; i < numcases; i++)
	{
		int fands = 0;
		int c1, c2;
		inputfile >> c1;
		inputfile >> c2;
		//read line numcases + 1 from file
		for(int j = c1; j <= c2; j++)
		{
			bool fair = false;
			bool square = false;
		if(isfair(j))
		{
			fair = true;

		}		
			int sqr = sqrt(j);
			if((sqr*sqr) == j)
			{
			
			if(isfair(sqr))
			{
				square = true;
			}
		}
			if(fair && square)
			{
				fands++;
			}
		

		
		}	

		outputfile << "Case #" << i+1 << ": " << fands << "\n";
	}
	
outputfile.close();
inputfile.close();
	return 0;
}

