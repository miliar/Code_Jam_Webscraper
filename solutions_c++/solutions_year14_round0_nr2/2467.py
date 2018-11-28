#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
#include <iostream>
#include <fstream>
#include <Windows.h>

const double Pi = acos(-1.0);

#define li long int 

li myCeilDiv(li num, li divBy){
	li res=num/divBy;
	if (num%divBy!=0){
		res++;
	}
	return res;

}

using namespace std;

// generic solution
template <class T>
int numDigits(T number)
{
    int digits = 0;
    if (number < 0) digits = 1; // remove this line if '-' counts as a digit

    while (number) {
        number /= 10;
        digits++;
		if (number<1){
			return digits;
		}
    }
    return digits;
}

const std::string inputPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\qualification round 2014\\B Cookie Clicker Alpha\\B-small-attempt0.in";
const std::string outPath = "C:\\Users\\Rayee\\Dropbox\\Google Code Jam\\qualification round 2014\\B Cookie Clicker Alpha\\B-small-attempt0.out";

//Globals

double timeToWinWithProdRate(double newProdRate, double X){
	double res=X/newProdRate;
	return res;
}

/************************************************************************/
/* solves the case
*/
/************************************************************************/

double solveCase (double C, double F, double X){
	double curCookies=0;
	double curProdRate=2;
	double cookiesToMake;
	double timeToFarm;
	double timeToWin;
	double timePassed=0;
	double tmpTime, timeWithNewRate, timeSpentToBuy;

	while (true){
		timeToFarm=C/curProdRate;
		cookiesToMake=X-curCookies;
		timeToWin=cookiesToMake/curProdRate;

		//only make decision when you can buy a fram
		//assert(timeToFarm<=timeToWin);

		//if it is worthy to buy a farm-> reach for it
		timeWithNewRate=timeToWinWithProdRate(curProdRate+F, X);
		
		if(timeToFarm+timeWithNewRate < timeToWin){
			//go to buy farm
			curCookies=0;
			curProdRate=curProdRate+F;
			timePassed+=timeToFarm;
		}
		else{//it is better to go stargiht for the win
			tmpTime=timeToWinWithProdRate(curProdRate,X);
			timePassed+=tmpTime;
			return timePassed;
		}
	}

	//return 4;
}

/*
Main
*/

int main() {

	int numCases, caseNum = 1;
	double result;
	double C,F,X;

	ifstream myfile(inputPath.c_str());
	ofstream resFile(outPath.c_str());
	
	//first line : number of cases
	myfile >> numCases;
	
	//vars for that question
	int firstRow, secondRow, num;

	//read all cases
	for (int i = 1; i <= numCases; ++i){
				
		myfile >>C;
		myfile >>F;
		myfile >>X;
		
		result=solveCase(C,F,X);
		
		long numOfDigits=numDigits(result);
		resFile.precision(7+numOfDigits);
		resFile << "Case #" << i << ": " << result << endl;
		
		//zero globals if needed

	}//end for

	myfile.close();
	resFile.close();

	return 0;

}


