#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <iomanip>


//Input and Output Files
std::ifstream reader ("C:\\codejam\\input.in");
std::ofstream writer("C:\\codejam\\output.out");

int main()
{
	//Check files are ok
	if (!reader)
	{
		std::cout << "Error opening file for input" << std::endl;
		return -1;
	}
	if (!writer)
	{
		std::cout << "Error opening file for output" << std::endl;
		return -1;
	}
	

	int Total = 0;
	int Required = 0;
	int TotalRequired = 0;
	int T;
	int X;
	int S =0;
	char numPeople[10000];

	reader >> T;

	for(int i=0;i<T;i++)
	{
		reader >> X;		
		reader >> numPeople;

		for(int k=0;k<=X;k++)
		{
			S = numPeople[k] - 48;
			Required = k - Total;
			if(Required > 0)
			{
				TotalRequired = TotalRequired + Required;
				Total = Total + Required;
			}
			Total = Total + S;
		}
		
		writer << "Case #" << i + 1 << ": ";
		writer << TotalRequired;
		writer << std::endl;
		Total = 0;
		TotalRequired = 0;
		Required = 0;
	}
	
	//Clean Up
	reader.close();
	writer.close();
	return 0;
}
