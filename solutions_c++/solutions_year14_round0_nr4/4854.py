// Codejam3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

void GetDeceitFulWarOutput(int nNoOfweights,double* dGirlsWeights,double* dBoysWeights,int ncaseNo,FILE* outfile)
{
	int nWarWins = nNoOfweights;
	int nDecietWarWins=0;
	std::vector<double> vec;
	for(int count=0;count <nNoOfweights;count++)
	{
		vec.push_back(dBoysWeights[count]);
	}

	std::vector<double> vecGirl;
	for(int count=0;count <nNoOfweights;count++)
	{
		vecGirl.push_back(dGirlsWeights[count]);
	}
	//Find War Wins
	/*for(int nIndex = 0; nIndex <nNoOfweights; nIndex++)
	{
		if(dGirlsWeights[nIndex] > dBoysWeights[nIndex])
			nWarWins++;
	}	*/
	int nNoOfVecCount=nNoOfweights;
	for(int nIndex = 0; nIndex <nNoOfweights; nIndex++)
	{
		int flag = 0;
		int nPos=0;
		for(; nPos < nNoOfVecCount; nPos++)
		{
			
			if(dGirlsWeights[nIndex] < vec[nPos])
			{
				flag = 1;
				vec.erase(vec.begin() + nPos);
				nNoOfVecCount--;
				break;
			}
		}
		if(flag == 1)
		{			
			nWarWins--;
		}
	}

	nNoOfVecCount=nNoOfweights;
	for(int nIndex = 0; nIndex <nNoOfweights; nIndex++)
	{
		//int flag = 0;
		for(int nPos = 0; nPos <nNoOfVecCount; nPos++)
		{
			
			if(dBoysWeights[nIndex] < vecGirl[nPos])
			{
				vecGirl.erase(vecGirl.begin() + nPos);
				nNoOfVecCount--;
				nDecietWarWins++;				
				break;
			}
		}
		/*if(flag == 1)
		{
			nDecietWarWins--;
		}*/
	}

	fputs("Case #",outfile);
	fprintf_s(outfile,"%d",ncaseNo);
	fputs(": ",outfile);
	fprintf_s(outfile,"%d",nDecietWarWins);
	fprintf_s(outfile," %d",nWarWins);
	fputs("\n",outfile);
	cout<<"War Wins::"<<nWarWins<<endl;
	cout<<"Deciet War Wins::"<<nDecietWarWins;

}

void SortArray(double* boysWeights,int ncount)
{
	for (int i = 0; i < ncount; ++i)
	{
		for (int j = i + 1; j < ncount; ++j)
		{
			if (boysWeights[i] > boysWeights[j])
			{
				double temp =  boysWeights[i];
				boysWeights[i] = boysWeights[j];
				boysWeights[j] = temp;
			}
		}
    }
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *file=fopen("input.in","r");	
	FILE *outFile=fopen("output.txt","w");
	char line[255] ={"\0"};	
	int nNoOfInput=0,nNoOfweights=0;
	double dGirlsWeights[1100], dBoysWeights[1100];
	int ncaseNo=1;
	//get number of input	
	if(fgets ( line, sizeof line, file ) != NULL )
	{
		nNoOfInput=atoi(line);
	}
		
	bool bArray1=true;
	while(fgets ( line, sizeof line, file ) != NULL )
	{
		nNoOfweights=atoi(line);
		char seps[]   = " ";
		for(int npeoplecount=0;npeoplecount<2;npeoplecount++)
		{
			if(fgets ( line, sizeof line, file ) != NULL )
			{
				char* token = strtok( line, seps );
				for(int ncount=0;ncount<nNoOfweights;ncount++)
				{
					// While there are tokens in "string"
					if(bArray1)
						dGirlsWeights[ncount]=atof(token);
					else
						dBoysWeights[ncount]=atof(token);				 

					// Get next token: 
					token = strtok( NULL, seps ); 
				}			  
			}
			bArray1=!bArray1;
		}
		if(bArray1 && (ncaseNo <= nNoOfInput))
		{
			SortArray(dBoysWeights,nNoOfweights);
			SortArray(dGirlsWeights,nNoOfweights);
			GetDeceitFulWarOutput(nNoOfweights,dGirlsWeights,dBoysWeights,ncaseNo,outFile);
			ncaseNo++;
		}
	}
	

	
return 0;
}

