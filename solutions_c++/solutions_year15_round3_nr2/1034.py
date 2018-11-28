// CodeJam2015_B.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <set>
#include <string>


using namespace std;

string Keys,Target,Trial;
long long int N(0),MaxT(0),NumT(0);
int K,L,S;

void Check(string SoFar) 
{
	if(SoFar.length()==S) {
		N++;
		// look for target in S
		int CurPos=0,CurHits(0);
		while(string::npos !=(CurPos = SoFar.find(Target,CurPos))) {
			CurPos++; // not again
			CurHits++;
		}
		NumT+=CurHits;
		MaxT = max(MaxT,(long long int)CurHits);
	}
	else {
		for(string::const_iterator it(Keys.begin()); it != Keys.end(); it++) {
			Check(SoFar + *(it));
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cin >> K >> L >> S;
		cin >> Keys >> Target;
		double Res(1);
		// check possible
		MaxT=NumT=N=0;

		for(string::iterator it(Target.begin());it != Target.end()&&N>=0; it++)
			if( Keys.find(*it) == string::npos) N=-1;
		if(N==-1) Res = 0;
		else {
			Check( "");
			Res = MaxT-((double)NumT/N);
		}
		cout << "Case #" << NumCase << ": " << setprecision(12) << Res;
		cout << endl;
	}
	return 0;
}

