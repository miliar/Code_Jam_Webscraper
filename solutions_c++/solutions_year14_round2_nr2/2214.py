//============================================================================
// Name        : Lottery.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int casos;
	cin >> casos;
	for (int caso = 1; caso <= casos; caso++)
	{
		unsigned int a, b, k;
		cin >> a >> b >> k;
		int c = 0;
		for (int ai = 0; ai < a; ai++)
			for (int bi = 0; bi < b; bi++)
				if ((ai & bi) < k)
					c++;
		cout << "Case #" << caso << ": " << c << endl;
	}
}
