#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int main()
{
	cout << "Enter name of input file: ";
	string infilename;
	cin >> infilename;
	ifstream infile(infilename.c_str());

	cout << "Enter name of output file: ";
	string outfilename;
	cin >> outfilename;
	ofstream outfile(outfilename.c_str());
	
	
	int numCase, line1, line2;
	int line1nums[4];
	int line2nums[4];
	int dummy[4];
	
	infile >> numCase;
	//cout << numCase << endl;
	
	for (int i = 1; i <= numCase; i++)
	{
		infile >> line1;
		//cout << line1 << endl;
		for (int j = 1; j <=4; j++)
		{
			if(j != line1)
			{
				for (int k = 0; k <=3; k++)
				{
					infile >> dummy[k];
				}
			
			}
			
			else
			{
				for (int k = 0; k <=3; k++)
				{
					infile >> line1nums[k];
				}
			}
		}
		//cout << line1nums[0] << ' ' << line1nums[1] << endl;
		infile >> line2;
		//cout << line2 << endl;
		for (int j = 1; j <=4; j++)
		{
			if(j != line2)
			{
				for (int k = 0; k <=3; k++)
				{
					infile >> dummy[k];
				}
			
			}
			
			else
			{
				for (int k = 0; k <=3; k++)
				{
					infile >> line2nums[k];
				}
			}
		}
		//cout << line2nums[0] << ' ' << line2nums[1] << endl;
		int matches = 0;
		int match;
		
		for (int s = 0; s <=3; s++)
		{
			
			if (line1nums[s] == line2nums[0] || line1nums[s] == line2nums[1] || line1nums[s] == line2nums[2] || line1nums[s] == line2nums[3]   )
			{
				matches++;
				match = line1nums[s];
			}
		
		}
		
	if (matches == 0)	
		outfile << "Case #" << i << ": " << "Volunteer cheated!" <<endl;
	
	if (matches == 1)
		outfile << "Case #" << i << ": " << match <<endl;
		
	if (matches >= 2)
		outfile << "Case #" << i << ": " << "Bad magician!" <<endl;
	
	}
	
	



return 0;
}