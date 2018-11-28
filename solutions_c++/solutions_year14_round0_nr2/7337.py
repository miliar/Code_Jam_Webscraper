#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;
int main()
{
	double C,F,X;
	double rate = 2;
	double sec = 0;
	int TC=1;
	int noOfTestcases;
	fstream dataFile;
	ofstream out;
	dataFile.open("B-large.in");
	out.open("output.txt");
	if(!dataFile)
	{
		cout << "File Not Found" << endl;
		exit(0);
	}
	dataFile >> noOfTestcases;
	for(int i = 0 ; i < noOfTestcases ; i++)
	{
		dataFile >> C >> F >> X;
		while(1)
		{
			if ((X/rate) <= ((C/rate)+(X/(rate+F))))
			{
				sec = sec + X/rate;
				break;
			}
			else
			{
				sec = sec + C/rate;
				rate = rate + F;
			}
		}
		out << "Case #" << TC << ": " << setprecision(7) << fixed << sec << endl;
		sec = 0;
		rate = 2;
		TC++;
	}
	return 0;
}