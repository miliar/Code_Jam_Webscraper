// Sheep.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		
		cout << "Case #" << NumCase << ": " ;
		unsigned long long int N(0),TestN, CurN;
		int Digs[10], CurDig;
		for(CurDig=0;CurDig<10;CurDig++) Digs[CurDig]=0;
		cin >> N;
		if(N==0) cout << "INSOMNIA";
		else 
		{
			CurN = N;
			int DigsSeen;
			do {
				TestN = CurN;
				while(TestN>0) {
					unsigned long long int TN10 = TestN/10;
					unsigned long long int TN = TN10 * 10;
					Digs[TestN-TN] = Digs[TestN-TN] | 1; 
					TestN = TN10;
				}
				for(DigsSeen=1,CurDig=0;DigsSeen && CurDig<10;CurDig++) DigsSeen = DigsSeen && Digs[CurDig];
				if(DigsSeen) {
					cout << CurN;
					break;
				}
				CurN += N;
			}while(CurN<ULONG_MAX/2);
		}
		cout << endl;
	}

	return 0;
}

