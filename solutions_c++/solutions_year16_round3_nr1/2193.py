// CodeJam4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<fstream>
#include <algorithm>

using namespace std;
class Problem {
public:
	Problem() {

	}
};
int main()
{
	ifstream f;
	ofstream g;
	int problems = 0;
	int ile = 0;
	bool done = false;
	int *tab;
	int max = 0;
	int value = 0;
	int temp = 0;
	f.open("problem.in");
	g.open("answear.out");
	f >> problems;
	for (int i = 0; i < problems; i++) {
		f >> ile;
		tab = new int[ile];
		for (int x = 0; x < ile; x++) {		//czytanie
			f >> tab[x];
		}
		done = false;
		g << "Case #" << i + 1 << ": ";
		while (!done) {
			max = distance(tab, max_element(tab, tab + ile));
			value = tab[max];
			if (value != 0) {
				tab[max]--;
				g << (char)(65 + max);
				max = distance(tab, max_element(tab, tab + ile));
				if (value == tab[max] ) {
					if (tab[max] != 1) {
						tab[max]--;
						g << (char)(65 + max);
					}
					else {
						temp = max;
						tab[max]--;
						max = distance(tab, max_element(tab, tab + ile));
						if (tab[max] == 1) tab[temp]++;
						else g << (char)(65 + temp);
					}
					
				}
				g << " ";
			}
			else {
				g << endl;
				done = true;
			}

		}
		delete tab;

	}
	return 0;
}

