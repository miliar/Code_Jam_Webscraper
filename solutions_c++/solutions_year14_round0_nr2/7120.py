#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <iomanip>

//Input and Output Files
std::ifstream reader ("C:\\Users\\Dave\\Downloads\\B-large.in");
std::ofstream writer("C:\\Users\\Dave\\Documents\\Code Jam\\2014\\cookie-clicker-alpha.out");

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
	
	double C; //Cookies needed for a farm
	double F; //Extra cookies per second with another farm
	double X; //Cookies needed to win
	int T = 0; //Test cases
	double Rate;
	double dbtemp;
	double dbtemp2; 
	double prevTotal;
	double runTotal;

	reader >> T;

	for(int i=0;i<T;i++)
	{
		C = 0;
		F = 0;
		X = 0;

		Rate = 2.0;

		dbtemp = 0;
		dbtemp2 = 0;
		prevTotal = 0; 
		runTotal = 0;

		reader.precision (15);
		reader >> std::fixed >> C;
		reader >> std::fixed >> F;
		reader >> std::fixed >> X;

		runTotal = X;

		for(int k=0;k<100000;k++)
		{
		//Time taken to produce total cookies at current rate
		dbtemp = X / Rate;
		
		prevTotal = runTotal;
		runTotal = dbtemp + dbtemp2;

		if(runTotal > prevTotal)
		{
			break;
		}
		dbtemp2 += C / Rate;
		Rate = Rate + F;
		}

		writer << "Case #" << i + 1 << ": ";
		writer.precision (7);
		writer << std::fixed << prevTotal;
		writer << std::endl;
	}
	
	//Clean Up
	reader.close();
	writer.close();
	return 0;
}
