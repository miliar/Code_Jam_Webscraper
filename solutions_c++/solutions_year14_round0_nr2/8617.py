//
//  main.cpp
//  CookieClickerAlpha
//
//  Created by Patrick Burns on 4/12/14.
//  Copyright (c) 2014 Bl4ckSun. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <unistd.h>
#include <iomanip>
using namespace std;

#if 0
string filename = "sample.in";
string resultsFile = "codeJamResults-sample.out";
#elif 0
string filename = "small.in";
string resultsFile = "codeJamResults-small.out";
#elif 1
string filename = "large.in";
string resultsFile = "codeJamResults-large.out";
#endif

ifstream inFile;
ofstream outFile;

// T = Test Cases

int numberOfTest;

double cookieRate;
double costOfFarm;
double costOfComplete;

double numberOfFarms;
double totalTime;
double bestTime;

double timeToComplete;
double timeToFarm;

bool go;

int main(int argc, const char * argv[])
{
	chdir("/Users/p8burns/Development/GoogleCodeJam/2014/QualificationRound/CookieClickerAlpha");
	inFile.open(filename);
	outFile.open(resultsFile);
	
	cout << "Hello world" << endl;
	cout.precision(7);
	outFile.precision(7);
	
	inFile >> numberOfTest;
	for(int testNumber = 1; testNumber <= numberOfTest; testNumber++)
	{
		inFile >> costOfFarm;
		inFile >> cookieRate;
		inFile >> costOfComplete;
		
		go = true;
		numberOfFarms = 0.0;
		totalTime = 0.0;
		
		bestTime = costOfComplete / (2.0 + (cookieRate * numberOfFarms)) + totalTime;
		
		do{
			timeToFarm		= costOfFarm / (2.0 + (cookieRate * numberOfFarms));
			timeToComplete	= costOfComplete / (2.0 + (cookieRate * numberOfFarms));
			
//			cout << "To Farm: " << timeToFarm << " To Complete: " << timeToComplete << endl;
						
			if(timeToComplete + totalTime < bestTime)
				bestTime = timeToComplete + totalTime;
			else if(timeToFarm + totalTime > bestTime )
				go = false;
			
			totalTime += timeToFarm;

			numberOfFarms = numberOfFarms + 1.0;
			
		}while (go);
		
//		cout <<  std::setprecision(9) << "C: " << costOfFarm << " F: " << cookieRate << " X: " << costOfComplete << endl;

		cout << "Case #" << testNumber << ": " << fixed << bestTime << endl;
		outFile << "Case #" << testNumber << ": " << fixed << bestTime << endl;
	}
    return 0;
}
