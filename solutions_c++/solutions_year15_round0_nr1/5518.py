// ProblemA.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

//int _tmain(int argc, _TCHAR* argv[])

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int T=0;
	cin >> T;

	for (int x = 1; x <= T; x++) {
		cout << "Case #" << x << ": ";
		int y = 0;
		int Smax = 0;
		string S = "";
		cin >> Smax >> S;
		
		int tp=0;

		for (int i = 0; i<Smax+1; i++){
			int Si = S.c_str()[i] - '0';
			
			if (Si > 0){
				int p = i - tp;
				if (p>0){
					y += p;
					tp += p;
				}
				tp += Si;
			}
		}

		cout << y << endl;
		if (y > -1) {
			cerr << "at " << x << " case " << endl;
		}
	}
	return 0;
}

