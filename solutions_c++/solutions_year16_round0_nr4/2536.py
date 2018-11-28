// Fractal.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <bitset>

using namespace std;
const unsigned long MaxPrime = 1000000;
unsigned long Sieve[MaxPrime];

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		unsigned  K,C,S;
		cin >> K >> C >> S;
		cout << "Case #" << NumCase << ": " ;
		for(unsigned int i=0;i<S;i++) cout << i+1 << " ";
		cout << endl;
	}
	return 0;
}

