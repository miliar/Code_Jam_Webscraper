// CodeJamQues1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <Windows.h>
#include <string>
using namespace std;

void WriteOutput(int row1,int Array1[4][4],int row2,int Array2[4][4],int caseNo,FILE *file)
{	

	int nArrRow1[4];
	for(int nIndex = 0; nIndex <4 ; nIndex++)
	{
		nArrRow1[nIndex] = Array1[row1 - 1][nIndex];
	}
	

	int nArrRow2[4];
	for(int nIndex = 0; nIndex < 4 ; nIndex++)
	{
		nArrRow2[nIndex] = Array2[row2 - 1][nIndex];
	}

	//Now match 3 cases.
	
	int nNumMatch = 0;
	int nMatchedNumber = -1;
	for(int nIndex1 = 0 ; nIndex1 < 4; nIndex1++)
	{
		for(int nIndex2 = 0 ; nIndex2 < 4; nIndex2++)
		{
			if( nArrRow1[nIndex1] == nArrRow2[nIndex2])
			{
				nNumMatch++;
				nMatchedNumber = nArrRow1[nIndex1];
			}
		}
	}
	char chOutput[128];
	if(nNumMatch == 1)
	{		
		fputs("Case #",file);
		fprintf_s(file,"%d",caseNo);
		fputs(": ",file);
		fprintf_s(file,"%d",nMatchedNumber);		
	}
	else if(nNumMatch > 1)
	{
		fputs("Case #",file);
		fprintf_s(file,"%d",caseNo);
		fputs(": ",file);		
		fputs("Bad magician!",file);		
	}
	else
	{
		fputs("Case #",file);
		fprintf_s(file,"%d",caseNo);		
		fputs(": ",file);
		fputs("Volunteer cheated!",file);		
	}
	fputs("\n",file);
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *file=fopen("input.in","r");		
	cout<<GetLastError();
	FILE *outFile=fopen("output.txt","w");
	char line[255] ={"\0"};
	size_t len=0;
	char read;
	int nNoOfInput=0,nrowNo1=0,nrowNo2=0;
	int nArray1[4][4],nArray2[4][4];
	int ncaseNo=1;
	//get number of input	
	if(fgets ( line, sizeof line, file ) != NULL )
	{
		nNoOfInput=atoi(line);
	}
		
	bool bArray1=true;
	while(fgets ( line, sizeof line, file ) != NULL )
	{
		if(bArray1)
			nrowNo1=atoi(line);
		else
          nrowNo2=atoi(line);
		
		for(int ncount=0;ncount<4;ncount++)
		{			
			char seps[]   = " ";
			if(fgets ( line, sizeof line, file ) != NULL )
			{
				char* token = strtok( line, seps );
				for(int ncount1=0;ncount1<4;ncount1++)
				{
					// While there are tokens in "string"
					if(bArray1)
						nArray1[ncount][ncount1]=atoi(token);
					else
						nArray2[ncount][ncount1]=atoi(token);				 

					// Get next token: 
					token = strtok( NULL, seps ); 
				}			  
			}
		   }
		bArray1=!bArray1;
		if(bArray1 && (ncaseNo <= nNoOfInput))
		{
           WriteOutput(nrowNo1,nArray1,nrowNo2,nArray2,ncaseNo,outFile);
		   ncaseNo++;
		}

	}
	return 0;
}

