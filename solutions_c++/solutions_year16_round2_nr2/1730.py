#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

using namespace std;

void search(int Cconst, int Jconst, set<int> C, set<int> J, int& mina,int&minc,int&minj,int&resc,int&resj) {
	if(! C.empty() ) {
		int CurC = *C.begin();
		C.erase(C.begin());
		for(int i=0; i<10; i++) {
			Cconst += i*CurC;
			search(Cconst, Jconst, C, J, mina, minc, minj, resc, resj);
			Cconst -= i*CurC;
		}
		C.insert(CurC);
	} else if( ! J.empty() ) {
		int CurJ = *J.begin();
		J.erase(J.begin());
		for(int i=0; i<10; i++) {
			Jconst += i*CurJ;
			search(Cconst, Jconst, C, J, mina, minc, minj, resc, resj);
			Jconst -= i*CurJ;
		}
		J.insert(CurJ);
	}
	if(abs(Cconst-Jconst)<mina) {
		mina = abs(Cconst-Jconst);
		minc = resc = Cconst;
		minj = resj = Jconst;
	}
	if(abs(Cconst-Jconst) == mina) {
		if(Cconst < minc) {
			minc = resc = Cconst;
			minj = resj = Jconst;
		}
		else if( Cconst == minc ) {
			if(Jconst<minj) {
				resj = minj = Jconst;
			}
		}
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cout << "Case #" << NumCase << ": ";
		int Cconst(0), Jconst(0),Decimal;
		set<int> C,J;
		string Cin, Jin;
		cin >> Cin >>Jin;
		Decimal=1;
		for(string::const_reverse_iterator it = Cin.rbegin(); it != Cin.rend(); it++) {
			const char x(*it);
			if(x == '?') C.insert(Decimal); else Cconst += (x-'0')*Decimal;
			Decimal*=10;
		}
		Decimal=1;
		for(string::const_reverse_iterator it = Jin.rbegin(); it != Jin.rend(); it++) {
			if(*it == '?') J.insert(Decimal); else Jconst += (*it-'0')*Decimal;
			Decimal*=10;
		}
		int mina(1000),minc(1000),minj(1000),resc(0),resj(0);
		search(Cconst, Jconst, C, J,mina,minc,minj,resc,resj);
		cout << setfill('0') << setw(Cin.length()) << resc << ' ' << setfill('0') << setw(Cin.length()) << resj << setw(0) << endl;
	}
	return 0;
}
