// StandingOvation.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		int SMax,Res(0),Standing(0);
		int SL;
		cin >> SMax;
		for( int i=0; i <= SMax; i++) { 
			char in;
			cin >> in;
			SL = in - '0';
			if(Standing>=i) Standing+=SL;
			else if (SL>0) {
				Res+=i-Standing;
				Standing = i+SL;
			}
		}

		cout << "Case #" << NumCase << ": " << Res;
		cout << endl;
	}
	return 0;
}
