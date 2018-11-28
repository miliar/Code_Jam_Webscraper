#include <iostream>
#include <string>
#include <math.h>
#include <memory.h> 
#include <fstream>
#include <sstream>
#include <vector>
#include<iomanip> 
#include<algorithm> 
using namespace std; 

//#define   inFile infile
//#define   outFile cout


int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt0.in");
	outfile.open("c-large-1.out");

	int num_cases;
	infile>>num_cases;


	for (int j = 1; j <= num_cases; j++)
	{
		int first;
		int second;
		int square1st[4];
		int square2nd[4];
		infile>>first;
		int discard;
		for (int i = 0; i != 4*(first - 1); ++i)
		{
			infile>>discard;
		}
		for (int m = 0; m != 4; ++m)
		{		
			infile>>square1st[m];
		}
		for (int i = 0; i != 16 - 4 - 4*(first - 1); ++i)
		{
			infile>>discard;
		}
		infile>>second;
		for (int i = 0; i != 4*(second - 1); ++i)
		{
			infile>>discard;
		}
		for (int m = 0; m != 4; ++m)
		{		
			infile>>square2nd[m];
		}
		for (int i = 0; i != 16 - 4 - 4*(second - 1); ++i)
		{
			infile>>discard;
		}
		int same_num = 0;
		int num = 0;
		for (int m = 0; m != 4; ++m)
		{
			for (int n = 0; n != 4; ++n)
			{
				if (square1st[m] == square2nd[n])
				{
					same_num++;
					num = square2nd[n];
				}
			}
		}
		outfile<<"Case #"<<j<<": ";
		if (same_num == 1)
			outfile<<num;
		else if(same_num > 1)
		{
			outfile<<"Bad magician!";
		}
		else if (same_num == 0)
		{
			outfile<<"Volunteer cheated!";
		}
		outfile<<endl;

	}
	return 0;
}

