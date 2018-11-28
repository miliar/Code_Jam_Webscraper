/*
 * .cpp
 * 
 *
 ******************************************************************************
 *
 ******************************************************************************
 * Pre: 
 *
 * Post:
 *
 ******************************************************************************
 *  Created on: 12-abr-2015
 *      Author: Abel Serrano Juste
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int cases_nr,X,R,C;
	
	cin >> cases_nr;
	
	for (int i=1; i<=cases_nr; ++i) {
		cin >> X >> R >> C;
		cout << "case #" << i <<": ";
		
		if (X==1)
			cout << "GABRIEL";
		else if (R*C < X)
			cout << "RICHARD";
		else if ((R * C) % X)
			cout << "RICHARD";
		else if (X>2 && (R==1 || C==1))
		  cout << "RICHARD";
		else if (X==2)
			cout << "GABRIEL";
		else if (X==3 && (R*C==6 || R*C==12 || R*C==9))
			cout << "GABRIEL";
		else if (X==4 && (R==4 && 4==C))
			cout << "GABRIEL";
		else if (X==4 && ( (R==3 && 4==C) || (R==4 && 3==C)) )
			cout << "GABRIEL";
		else if (X==4)
			cout << "RICHARD";
		
		//else -> only some cases with X==3 left to do by hand. else is considerated above. 
		cout << endl;
	}
	
	return 0;
}

