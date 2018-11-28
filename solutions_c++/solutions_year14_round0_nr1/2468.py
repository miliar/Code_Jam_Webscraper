#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#include<iostream>
#include<fstream>

int main() 
{
	ifstream fpInput("C:\\Users\\ametpall\\Downloads\\A-small-attempt3.in", ios::in);
	ofstream fpOutput("C:\\Output.txt", ios::out);
	int tc; fpInput>>tc;
	for(int tci = 0; tci < tc; tci++) 
	{
		fpOutput<<"Case #"<< tci+1<<": ";
		
		int iChoice1 ;
		fpInput>>iChoice1;
		int iAgment1[16];
		for(int iIndex=0;iIndex<16;iIndex++)
			fpInput>>iAgment1[iIndex];

		int iChoice2 ;
		fpInput>>iChoice2;
		int iAgment2[16];
		for(int iIndex=0;iIndex<16;iIndex++)
			fpInput>>iAgment2[iIndex];

		int iCount = 0;
		int iVal = 0;
		for(int iInner = 0; iInner <=3; iInner++)
		{
			if( (iAgment1[((iChoice1-1)*4 + iInner)] == iAgment2[((iChoice2-1)*4 + 0)]) || 
				(iAgment1[((iChoice1-1)*4 + iInner)] == iAgment2[((iChoice2-1)*4 + 1)]) ||
				(iAgment1[((iChoice1-1)*4 + iInner)] == iAgment2[((iChoice2-1)*4 + 2)]) ||
				(iAgment1[((iChoice1-1)*4 + iInner)] == iAgment2[((iChoice2-1)*4 + 3)]) )
			{
				iCount++;
				iVal = iInner;				
			}
		}			
		
		if(iCount == 0)
			fpOutput<<"Volunteer cheated!";
		else if(iCount > 1)
			fpOutput<<"Bad magician!";
		else if(iCount == 1)
			fpOutput<<iAgment1[((iChoice1-1)*4 + iVal)];

		fpOutput<<"\n";

	}
	
	 return 0;
}