//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>


using namespace std;

int main() {
	ifstream fi;
	ofstream fo;
	//fi.open ("A.inp");
	fi.open ("A-small-attempt1.in");
	fo.open ("Ares.out");
	long long tural = 2000000000000000000;
	int tn;
	fi >> tn;
	long long r, L, k;
	for (int ti = 0; ti<tn; ti++){
		fi >> r >> L;

		k = 1;
		while (L >= 0){
			L -= 2*(r)+4*k -3;
			k++;
		}
		fo << "Case #" << ti+1 << ": " << k-2 << endl;

	}
	fi.close();
	fo.close();
	return 0;
}
