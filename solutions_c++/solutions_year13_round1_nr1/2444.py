#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

string filename("ProblemA_Data_Small.txt");
int main()
{
	ifstream infile(filename.c_str());
	if (infile)
    {
		ofstream outfile((string("Output_")+filename).c_str());
		if (outfile)
		{
			// read the input file
			int T;
			infile>>T;
			for (int icase = 1; icase <= T; icase++)
			{
				unsigned long int r,t; 
				infile>>r;
				infile>>t;
					
				
				unsigned long int k;
				k = floor(sqrt((double)0.5*t+(2*r-1)*(2*r-1)/16.0)-0.25*(2*r-1));
				
				
				outfile << "Case #"<<icase<<": "<<k<<endl;
			}
			
		}else{cout<<"Cannot create output file.\n"; return -1;}
    }else{cout<<"Cannot read the input file.\n"; return -1;}
	return 0;
}
