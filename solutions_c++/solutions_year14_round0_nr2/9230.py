#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>

using namespace std;

ifstream input;

double findZeAnzer(double C, double F, double X)
{
	double fAnswer = 0.0f;
	double fHowManySecondsForC;
	double fHowManySecondsForX;
	double fNextHowManySecondsForX;
	double fCurrentProductionRate = 2.0f;
	bool bGotTheAnswer = false;

 	while(!bGotTheAnswer)
 	{
 		fHowManySecondsForC = C / fCurrentProductionRate;
 		fHowManySecondsForX = X / fCurrentProductionRate;
 		fNextHowManySecondsForX = X / (fCurrentProductionRate + F);

 		if (fHowManySecondsForX < (fHowManySecondsForC + fNextHowManySecondsForX))
 		{
			bGotTheAnswer = true;
 			fAnswer += fHowManySecondsForX;
 		}
 		else
 		{
 			fAnswer += fHowManySecondsForC;	
 		}
 		
 		fCurrentProductionRate += F;
 	}

	return fAnswer;
}

int cookieClick(const char* filename)
{
	input.open(filename);

	if (!input.is_open())
	{
		cout << "Something went very bad when reading the file :(" << endl;
		exit(EXIT_FAILURE);
	}

	int nNumberOfTests;
	double fC;
	double fF;
	double fX;
	double fAnswer;
	ofstream output;
	output.open("output");
	input >> nNumberOfTests;
	

	for (int i = 1; i <= nNumberOfTests; ++i)
	{

		input >> std::fixed >> setprecision(7) >> fC;
		input >> std::fixed >> setprecision(7) >> fF;
		input >> std::fixed >> setprecision(7) >> fX;

		fAnswer = findZeAnzer(fC, fF, fX);
		output << "Case #" << i << ": " << std::fixed << setprecision(7) << fAnswer << endl;
	}

	// Finally
	input.close();

	return 0;
}

int main(int argc, char const *argv[])
{
		if( argc != 2)   
  { 
   cout <<" Usage: cookie <<input>>" << endl;
   exit(EXIT_FAILURE);
  }

  cookieClick(argv[1]);

	return 0;
}