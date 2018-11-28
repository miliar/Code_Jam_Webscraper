// prA_rd1b.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>


using namespace std;

char l[100][100];
int  n[100][100];

int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		int N,L(0),MaxL(0);
		cin >> N;
		for(int i=0;i<N;i++) 
			for(int j=0; j<100;j++) {l[i][j]='\000';n[i][j]=0;}

		for(int i=0;i<N;i++) {
			string xstr;
			cin >> xstr;
			L=0;
			for(string::iterator x=xstr.begin();x != xstr.end();x++) {
				if(L && *x == l[i][L-1]) n[i][L-1]++;
				else {
					l[i][L]=*x;
					n[i][L]=1;
					L++;
				}
			}
			if(L>MaxL) MaxL = L;
		}
		int Ops=0;
		int i;
		for(i=0;i<MaxL;i++) {
			if(l[0][i] == l[1][i]) {
				int CurMin=n[0][i],CurMax=n[0][i];
				for(int j=1;j<N;j++) {
					if(n[j][i] < CurMin) CurMin=n[j][i];
					if(n[j][i] > CurMax) CurMax=n[j][i];
				}
				int CurOpt=10000;
				for(int Goal=CurMin;Goal<=CurMax;Goal++) {
					int CurOps(0);
					for(int j=0;j<N;j++)
						CurOps+=abs(n[j][i]-Goal);
					if(CurOps<CurOpt) CurOpt=CurOps;
				}


				Ops += CurOpt;
			}
//			if(l[0][i] == l[1][i]) Ops += abs(n[0][i]-n[1][i]);
			else break;
		}
		if(i==MaxL)
			cout << "Case #" << NumCase << ": " << Ops << endl;
		else
			cout << "Case #" << NumCase << ": " << "Fegla Won" << endl;

	}
	return 0;
}

