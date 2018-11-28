// prB_rd1b.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		unsigned long A,B,K,res(0);
		cin >> A >> B >> K;
		for(unsigned long int a=0; a<A;a++)
			for(unsigned long int b=0; b<B;b++)
				if((a&b)<K) res++;
			cout << "Case #" << NumCase << ": " << res << endl;
	}
	return 0;
}

