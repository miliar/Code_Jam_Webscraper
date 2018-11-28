// CodeJam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <Windows.h>
using namespace std;

//void GetCookieOutput(double fCookiesForFarm,double fRateInitial,double fFinalCookiesCountX,int ncaseNo,FILE *outputFile)
//{
//	double fRate;
//	double fPreviousTime, fNextTime;
//
//	fPreviousTime = fFinalCookiesCountX / 2;
//	fNextTime = (fCookiesForFarm/2) + (fFinalCookiesCountX/(2+fRateInitial));
//
//	double fPrevRate = 2;
//	fRate = 2 + fRateInitial;
//
//	double fTime = (fCookiesForFarm/2);
//	while(fPreviousTime > fNextTime)
//	{
//		fPreviousTime	= fTime + (fFinalCookiesCountX / fRate);
//		fNextTime		= fTime +  (fCookiesForFarm/fRate) + (fFinalCookiesCountX/(fRate+fRateInitial));
//
//		fTime			= fTime + /*(fCookiesForFarm/fPrevRate) +*/  (fCookiesForFarm/fRate);
//		fPrevRate = fRate;
//		fRate = fRate + fRateInitial;
//	}
//	fputs("Case #",outputFile);
//	fprintf_s(outputFile,"%d",ncaseNo);
//	fputs(": ",outputFile);
//	fprintf_s(outputFile,"%0.7lf",fPreviousTime);
//	fputs("\n",outputFile);
//
//}
//void WriteOutput(int Array1[1000],int count,int caseNo,FILE *file)
//{	
//	bool bgood=true;	
//	for(int nIndex = 0; nIndex <count ; nIndex++)
//	{
//		if(Array1[nIndex] == nIndex)
//		{
//         bgood=false;
//		 break;
//		}
//	}	
//	char chOutput[128];
//	if(bgood)
//	{		
//		fputs("Case #",file);
//		fprintf_s(file,"%d",caseNo);
//		//fputs((char*)caseNo,file);
//		fputs(": ",file);
//		fputs("GOOD",file);
//		
//	}
//	else
//	{
//		fputs("Case #",file);
//		fprintf_s(file,"%d",caseNo);
//		//fputs((char*)caseNo,file);
//		fputs(": ",file);		
//		fputs("BAD",file);
//		cout<<"Bad magician!";
//	}	
//	fputs("\n",file);
//}
void CalculatePairs(DWORD A,DWORD B, DWORD K,int caseNo,FILE *file)
{
    DWORD dwResult = 0;
    DWORD dwCurrResult = 0;

    for(DWORD nIndexA = 0; nIndexA < A; nIndexA++)
    {
        for(DWORD nIndexB = 0; nIndexB < B; nIndexB++)
        {
                dwCurrResult = 0;
                dwCurrResult = nIndexA & nIndexB;
                //Now match result with K
               
                if(dwCurrResult>=0 && dwCurrResult < K)
                    dwResult++;
        }
    }
	fputs("Case #",file);
	fprintf_s(file,"%d",caseNo);	
	fputs(": ",file);
	fprintf_s(file,"%ld",dwResult);	
	fputs("\n",file);

}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *file=fopen("input.in","r");	
	FILE *outFile=fopen("output.txt","w");
	char line[255] ={"\0"};		
	int nNoOfInput=0,nNoOfElement=0;	
	int ncaseNo=1;
	int nArray1[1000];
	double fCookiesForFarm=0, fRateInitial=0,fFinalCookiesCountX=0;
	//get number of input	
	if(fgets ( line, sizeof line, file ) != NULL )
	{
		nNoOfInput=atoi(line);
	}

	/*if(fgets ( line, sizeof line, file ) != NULL )
	{
		nNoOfInput=atoi(line);
	}*/
	//read=fscanf(file,"%s",line);	
	while(fgets ( line, sizeof line, file ) != NULL )
	{
		
		/*nNoOfElement=(int)line;		
		
		
			read=fscanf(file,"%s",line);*/
			char seps[]   = " ";
			/*if(read != EOF)
			{*/
				char* token = strtok( line, seps );
				for(int ncount1=0;ncount1<3;ncount1++)
				{
					// While there are tokens in "string"
					
						nArray1[ncount1]=atoi(token);								 

					// Get next token: 
					token = strtok( NULL, seps ); 
				}			  
			//}
		   
		
		if( (ncaseNo <= nNoOfInput))
		{
           CalculatePairs(nArray1[0],nArray1[1],nArray1[2],ncaseNo,outFile);
		   ncaseNo++;
		}
	}


	//while(fgets ( line, sizeof line, file ) != NULL )
	//{
	//	char seps[]   = " ";
	//		nNoOfElement=atoi(line);
	//		if(fgets ( line, sizeof line, file ) != NULL )
	//		{
	//			char* token = strtok( line, seps );
	//			for(int ncount1=0;ncount1<nNoOfElement;ncount1++)
	//			{
	//				// While there are tokens in "string"
	//				if(token != NULL)
	//				nArray1[ncount1]=atoi(token);	
	//				// Get next token: 
	//				token = strtok( NULL, seps ); 
	//			}
	//			if(ncaseNo <= nNoOfInput)
	//			{
	//				WriteOutput(nArray1,nNoOfElement,ncaseNo,outFile);
	//				ncaseNo++;
	//			}
	//		}
	//}
	fclose(file);
	fclose(outFile);
	return 0;
}

