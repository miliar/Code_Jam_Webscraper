// ConsoleApplication2.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;
/*
4
4 11111
1 09
5 110011
0 1*/





int main() {

	FILE *f, *fout;
	fopen_s(&f, "A-large.in", "r");
	fopen_s(&fout, "A-large.out", "w");

	int T=0;
	int Smax=0;
	vector<int> inv;
	char tmp=0;

	fscanf_s(f, "%d\n", &T);

	for (int t=0; t<T; t++) {
		fscanf_s(f, "%d ", &Smax);

		// Read the case
		inv.clear();
		for (int c=0; c<Smax+1; c++) {
			fscanf_s(f, "%c", &tmp);
			inv.push_back((int)tmp-48);
		}

		// Print the case
		//printf("%d ", Smax);
		//for (int i=0; i<Smax+1; i++)  {
		//	printf("%d", inv.at(i));
		//}
		//printf("\n");

		// Process the case
		int guest=0, total=0;
		for (int i=0; i<Smax+1; i++) {
			int nb=inv.at(i);
			// Increment nb guests if necessary
			if (i>total) {
				guest ++;
				total ++;
			}
			// Always increment total number of people
			total += nb;
		}

		printf("%d\n", guest);

		if (t<T-1)
			fprintf(fout, "Case #%d: %d\n", t+1, guest);
		else		
			fprintf(fout, "Case #%d: %d", t+1, guest);

		fscanf_s(f, "\n");
	}


	fclose(fout);
	fclose(f);

	return 0;
}


