#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <assert.h>
using namespace std;


long long solve(char A[200], char B[200])
{
	long long result = 0;
	
	//nb solution < 1000
	long nbSolBasic = 0;//1, 4, 9

	int lenA = strlen(A);
	int lenB = strlen(B);

	if(lenA <= 3)
	{
		long borneInf = atoi(A);
		long borneSup = 0;
		if(lenB >3)
			borneSup = 1000;
		else
			borneSup = atoi(B);

		if(borneInf==1)
			nbSolBasic++;
		if(4>=borneInf && 4<=borneSup)
			nbSolBasic++;
		if(9>=borneInf && 9<=borneSup)
			nbSolBasic++;
	}

	//solution 40..080..04
	long nbSol484 = 0;
	for(int i=lenA+1;i<lenB;i++)
	{
		if(i%2 == 1)
			nbSol484++;
	}

	if(lenA%2>=1 && lenA !=1)
	{//is A <= 4..8..4
		char sol484[200];
		sol484[0] ='4';
		sol484[lenA-1] ='4';
		sol484[lenA/2] ='8';
		sol484[lenA] =0;
		for(int i=1;i<(lenA/2)-1;i++)
		{
			sol484[i] ='0';
			sol484[lenA-1-i] ='0';
		}

		int cmpA = strcmp(A, sol484);
		int cmpB = (strlen(sol484) == lenB) ? strcmp(B, sol484) : 1;
		if(cmpA <=0 && cmpB >=0)
			nbSol484++;		
	}

	if(lenB%2==1 && lenB !=1)
	{//is B >= 4..8..4
		char sol484[200];
		sol484[0] ='4';
		sol484[lenB-1] ='4';
		sol484[lenB/2] ='8';
		sol484[lenB] =0;
		for(int i=1;i<(lenB/2)-1;i++)
		{
			sol484[i] ='0';
			sol484[lenB-1-i] ='0';
		}

		int cmpA = (strlen(sol484) == lenA) ? strcmp(A, sol484) : -1;
		int cmpB = strcmp(B, sol484);	
		if(cmpA <=0 && cmpB >=0 && lenB!=lenA)
			nbSol484++;			
	}


	//solution 10..020..01
	long nbSol121 = 0;

	for(int i=lenA+1;i<lenB;i++)
	{
		if(i%2 == 1)
			nbSol121++;
	}

	if(lenA%2==1 && lenA !=1)
	{//is A <= 1..2..1
		char sol121[200];
		sol121[0] ='1';
		sol121[lenA-1] ='1';
		sol121[lenA/2] ='2';
		sol121[lenA] =0;
		for(int i=1;i<(lenA/2)-1;i++)
		{
			sol121[i] ='0';
			sol121[lenA-1-i] ='0';
		}

		int cmpA = strcmp(A, sol121);
		int cmpB = (strlen(sol121) == lenB) ? strcmp(B, sol121) : 1;
		if(cmpA <=0 && cmpB >=0)
			nbSol121++;				
	}

	if(lenB%2==1 && lenB !=1)
	{//is B >= 1..2..1
		char sol121[200];
		sol121[0] ='1';
		sol121[lenB-1] ='1';
		sol121[lenB/2] ='2';
		sol121[lenB] =0;
		for(int i=1;i<(lenB/2)-1;i++)
		{
			sol121[i] ='0';
			sol121[lenB-1-i] ='0';
		}

		int cmpA = (strlen(sol121) == lenA) ? strcmp(A, sol121) : -1;
		int cmpB = strcmp(B, sol121);
		if(cmpA <=0 && cmpB >=0  && lenB!=lenA)
			nbSol121++;			
	}


	//solution 1..n..1 n is betwen 3 and 9
	/*
	long nbSol1n1 = 0;
	for(int i=lenA+1;i<lenB;i++)
	{
		if(i%2 == 1)
		{
			int sqrtLen = (i/2)+1;
			if(sqrtLen-2 >=0)
			{
				switch(sqrtLen-2)
				{
					case 0://121
						nbSol1n1++;
						break;
					case 1 :
						nbSol1n1+=2;
						break;
					case 2 :
						nbSol1n1+=2;
						break;
					case 3 :
						nbSol1n1+=4;
						break;
					case 4 :
						nbSol1n1+=4;
						break;
					case 5 :
						nbSol1n1+=8;
						break;
					case 6 :
						nbSol1n1+=8;
						break;
					case 7 :
						nbSol1n1+=16;
						break;
					default : //>7
						if((sqrtLen-2)%2==1)
							nbSol1n1+=;
						break;
				}
			}
			
		}
	}
	*/
	result = nbSolBasic + nbSol484 + nbSol121;

	return result;
}


int _tmain(int argc, _TCHAR* argv[])
{ 
/*
	while(true)
	{
		int i =0;
		i++;
	}
*/
	int numCase = 0;
	char A[200];
	char B[200];

	cin >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		cin >> A >> B;

		cout << "Case #" << (i+1) << ": ";

		cout << solve(A, B);

		cout << endl;
	}

	return 0;
}



