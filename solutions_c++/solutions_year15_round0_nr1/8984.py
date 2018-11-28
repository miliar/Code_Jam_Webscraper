
#include "StdAfx.h"
#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <stdlib.h>
#include <sstream>
#include <locale>
#include <stdio.h>

using namespace std;

#define TAB_ROWS 1001 // changer pour le largeset 1001


int main()
{
	ifstream in( "D:\\DEV\\INPUT\\A-large.in" );
	ofstream outfile( "D:\\DEV\\OUTPUT\\A-small2.out" );
	string line;
	getline(in, line);
	int numCases = atoi( line.c_str() );
 
	outfile.setf(ios::fixed);
	outfile.setf(ios::showpoint);
	outfile.precision(4);

	int aTab[TAB_ROWS];

	for (int ncases=0; ncases<numCases; ncases++)
	{ 
		getline(in, line); 
		for (int i=0; i<TAB_ROWS; i++)
		{
			aTab[i] = 0;
		}
		char * pch;
		char * szline = (char*)line.c_str();
		char * szS;
		pch = strtok(szline," ");
		int nMaxS = atoi( pch );
		int index=0;
		// Rempli le tableau
		while (pch != NULL)
		{
			szS = pch;
			pch = strtok(NULL," ");			
		}
		// Traite
		int nFriends = 0;
		int nPers = 0;
		char c = szS[0];
		nPers += atoi(&c);
		if (nPers == 0)
		{				
			nFriends = 1;
			nPers = 1;
		}
		for (int i=1; i<strlen(szS); i++)
		{
			if (nPers < i)
			{				
				nFriends += i - nPers;
				nPers += i - nPers;
			}
			char c = szS[i];
			nPers += atoi(&c);
		}

		outfile<<"Case #"<<ncases+1<<": "<<nFriends<<endl;
		
	}
	return 0;
}
