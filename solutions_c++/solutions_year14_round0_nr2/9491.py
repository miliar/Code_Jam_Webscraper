// Cookie.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <iomanip>



#define INPUT_FILENAME		"infile.txt"
#define OUTPUT_FILENAME		"outfile.txt"
#define STARTING_COOKIES	0.0f
#define STARTING_RATE		2.0f



struct TEST_CASE_T
{
	float cost;
	float addedRate;
	float goal;
};



float time1(int nUpgrades, float C, float F, float X)
{
	float sum=0.0f;
	for (int i=0; i<nUpgrades; i++)
		sum += 1.0f / (STARTING_RATE + F * (float)i);
	return C*sum;	
}



float time2(int nUpgrades, float C, float F, float X)
{
	return X / (STARTING_RATE + F * (float)nUpgrades);
}



float CalcTime(const TEST_CASE_T* tc) 
{
	int nUpgrades = 0;
	float bestTime = time1(nUpgrades, tc->cost, tc->addedRate, tc->goal) + time2(nUpgrades, tc->cost, tc->addedRate, tc->goal);
	bool stop=false;
	do 
	{
		nUpgrades++;
		float t1 = time1(nUpgrades, tc->cost, tc->addedRate, tc->goal);
		float t2 = time2(nUpgrades, tc->cost, tc->addedRate, tc->goal);
		stop = (t1 > bestTime);
		
		if (t1+t2 < bestTime)
			bestTime = t1+t2;		
	} 
	while (!stop);

	return bestTime;
}


	
void WriteOutputFile(const std::vector <TEST_CASE_T>* tc) 
{
	std::ofstream ofs(OUTPUT_FILENAME);

	for (int i=0; i<tc->size(); i++)
	{
		TEST_CASE_T tmp = tc->at(i);
				
		float t = CalcTime(&tmp);

		ofs << "Case #" << i+1 << ": ";
		ofs << std::setprecision(7) << std::fixed << t << "\n";
	}
	
	ofs.close();
}



void ReadInputFile(std::vector <TEST_CASE_T>& tc)
{
	std::ifstream ifs(INPUT_FILENAME);

	int nTestCases;

	ifs >> nTestCases;

	for (int i=0; i<nTestCases; i++)
	{
		TEST_CASE_T tmpTestCase;

		ifs >> tmpTestCase.cost >> tmpTestCase.addedRate >> tmpTestCase.goal;

		tc.push_back(tmpTestCase);
	}
	
	ifs.close();
}



int _tmain(int argc, _TCHAR* argv[])
{
	std::vector <TEST_CASE_T> testCases;

	ReadInputFile(testCases);	
	WriteOutputFile(&testCases);

	return 0;
}

