#include <cstdlib>
#include <iostream>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <fstream>
using namespace std;

ofstream myAns;
ifstream Qfile;

void Solve(int CaseNum)
{
	double C,F,X;
	double WaitToWin=0;
	double UpdateAndWait=0;
	double AllUpdateTimeCost=0;
	double UpdateTime=0;
	double RateNow=2.0;
	double RateNext=0;

	Qfile>>C;
	Qfile>>F;
	Qfile>>X;

	do
	{
		WaitToWin = AllUpdateTimeCost + X/RateNow ;
		UpdateTime = C/RateNow ;
		RateNext = RateNow+F ;
		UpdateAndWait = AllUpdateTimeCost + UpdateTime + X/RateNext ;

		if(WaitToWin > UpdateAndWait)
		{
			AllUpdateTimeCost+=UpdateTime;
			RateNow=RateNext;
		}
		else
		{
			break;
		}
	}while(1);


	myAns<<"Case #"<<CaseNum<<": ";
	myAns.precision(15);
	myAns<<WaitToWin;
	myAns<<endl;
}

int main(int argc, char *argv[])
{
	int T=0;
	int i=0;

	Qfile.open("B-large.in");
	myAns.open ("MyAnser.txt");
		
	Qfile>>T;	
	
	for(i=0; i<T; i++)	
	{						
		Solve(i+1);
	}
	myAns.close();
	Qfile.close();
    
	system("PAUSE");
    return EXIT_SUCCESS;
}
