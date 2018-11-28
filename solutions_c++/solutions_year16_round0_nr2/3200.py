// Pancakes.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
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
		string s;
		cin >> s;
		int NumChanges = 1;
		for(string::const_iterator it=s.begin();it < s.end()-1;it++) 
			if(*it != *(it+1)) 
				NumChanges++;
		cout << NumChanges - (*(s.end()-1) =='+' ? 1:0);
		cout << endl;
	}

	return 0;
}

