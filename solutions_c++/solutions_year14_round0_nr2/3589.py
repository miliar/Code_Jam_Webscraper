#include <iostream>
#include <string>
#include <math.h>
#include <memory.h> 
#include <fstream>
#include <sstream>
#include <vector>
#include<iomanip> 
#include<algorithm> 
#include <iomanip>
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
		__int64 time = 0;
		double C;
		double F;
		double X;
		infile>>C>>F>>X;
		double total = 0;
		if (X <= C)
		{
			total = X/2;
		}
		else
		{
	/*		int i = (X - C)/C;*/
			int i = 0;
		
			/*		for (int k = 0; k < i - 1; ++k)
			{
			total += C/(2 + F*(k +1));
			}*/
			double select1 = 0;
			double select2 = 0;
			do 
			{
				select1 = X/(2 + i*F);
				select2 = C/(2 + i*F) + X/(2 + (i + 1)*F);
				if (select2 < select1 )
				{
					total += C/(2 + (i)*F);
					++i;
				}
				else
				{
					total += select1;
				}
			}
			while (select1 > select2);
		}
		

	

		outfile<<setprecision(7) <<setiosflags(ios::fixed | ios::showpoint)<<"Case #"<<j<<": "<<total;

		outfile<<endl;

	}
	return 0;
}

