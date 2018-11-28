// CodeJam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

void GetCookieOutput(double fCookiesForFarm,double fRateInitial,double fFinalCookiesCountX,int ncaseNo,FILE *outputFile)
{
	double fRate;
	double fPreviousTime, fNextTime;

	fPreviousTime = fFinalCookiesCountX / 2;
	fNextTime = (fCookiesForFarm/2) + (fFinalCookiesCountX/(2+fRateInitial));

	double fPrevRate = 2;
	fRate = 2 + fRateInitial;

	double fTime = (fCookiesForFarm/2);
	while(fPreviousTime > fNextTime)
	{
		fPreviousTime	= fTime + (fFinalCookiesCountX / fRate);
		fNextTime		= fTime +  (fCookiesForFarm/fRate) + (fFinalCookiesCountX/(fRate+fRateInitial));

		fTime			= fTime + /*(fCookiesForFarm/fPrevRate) +*/  (fCookiesForFarm/fRate);
		fPrevRate = fRate;
		fRate = fRate + fRateInitial;
	}
	fputs("Case #",outputFile);
	fprintf_s(outputFile,"%d",ncaseNo);
	fputs(": ",outputFile);
	fprintf_s(outputFile,"%0.7lf",fPreviousTime);
	fputs("\n",outputFile);

}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *file=fopen("input.in","r");	
	FILE *outFile=fopen("output.txt","w");
	char line[255] ={"\0"};		
	int nNoOfInput=0;	
	int ncaseNo=1;
	double fCookiesForFarm=0, fRateInitial=0,fFinalCookiesCountX=0;
	//get number of input	
	if(fgets ( line, sizeof line, file ) != NULL )
	{
		nNoOfInput=atoi(line);
	}

	while(fgets ( line, sizeof line, file ) != NULL )
	{
		char seps[]   = " ";
		char* token = strtok( line, seps );
		for(int ncount1=0;ncount1<3;ncount1++)
		{
			// While there are tokens in "string"
			if(ncount1 == 0)
				fCookiesForFarm=atof(token);
			else if(ncount1 == 1)
				fRateInitial=atof(token);	
			else
				fFinalCookiesCountX=atof(token);

			// Get next token: 
			token = strtok( NULL, seps ); 
		}
		if(ncaseNo <= nNoOfInput)
		{
		  GetCookieOutput(fCookiesForFarm,fRateInitial,fFinalCookiesCountX,ncaseNo,outFile);
		  ncaseNo++;
		}
	}
	fclose(file);
	fclose(outFile);
	return 0;
}

