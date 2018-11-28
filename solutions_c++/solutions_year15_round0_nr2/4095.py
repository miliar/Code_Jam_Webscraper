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




void findmax(vector<int> V, int *maxx, int *imax) {
	int N = (int)V.size();
	*maxx = 0;
	
	int tmp = 0;

	for (int i=0; i<N; i++) {
		tmp = V[i];
		if (tmp>(*maxx)) {
			*maxx = tmp;
			*imax = i;
		}
	}
}


// Split the value at i in halves
void split_halves(vector<int> *Pi, int i) {
	int value = Pi->at(i);

	Pi->at(i) = (value % 2==0 ? value/2 : value/2+1);
	Pi->push_back(value/2);
}

// Split the value at i in halves
void split_thirds(vector<int> *Pi, int i) {
	int value = Pi->at(i);

	Pi->at(i) = (value/3);
	Pi->push_back(2*value/3);
}


// Backtrack
void backtrack( vector<int>Pi, int i, int *minutes, int tps) {

	int value = Pi[i];
	if (value<4)
		return;

	vector<int> Qi = Pi;

	int maxx=0, imax=0;
	
	split_halves(&Qi, i);

	// Get the new max
	findmax(Qi, &maxx, &imax);
	// Increment the time by 1
	//(*tps) ++;

	// Check if leaving everyone + time already spent with special minutes is better than previous best time
	if (maxx+ (tps+1) < *minutes)
		*minutes = maxx+ (tps+1);

	backtrack(Qi, imax, minutes, tps+1);
	
	
	// Split in thirds otherwise
	if (value%3==0) {		
		Qi = Pi;
		split_thirds(&Qi, i);

		// Get the new max
		findmax(Qi, &maxx, &imax);
		// Increment the time by 1
		//(*tps) ++;

		// Check if leaving everyone + time already spent with special minutes is better than previous best time
		if (maxx+ (1+tps) < *minutes)
			*minutes = maxx+ (1+tps);

		
		backtrack(Qi, imax, minutes, tps+1);
	}
	
}



int main() {

	FILE *f, *fout;
	fopen_s(&f, "data2/B-small-attempt1.in", "r");
	fopen_s(&fout, "data2/B-small-attempt1.out", "w");

	//fopen_s(&f, "data2/data2.txt", "r");
	//fopen_s(&fout, "data2/data2out.txt", "w");

	int T=0;
	int D=0;
	vector<int> Pi;
	int tmp=0;

	fscanf_s(f, "%d\n", &T);

	for (int t=0; t<T; t++) {
		fscanf_s(f, "%d\n", &D);

		// Read the case
		Pi.clear();
		int maxx=0, imax=0;
		for (int c=0; c<D; c++) {
			fscanf_s(f, "%d ", &tmp);
			Pi.push_back(tmp);

			if (tmp>maxx) {
				maxx = tmp;
				imax = c;
			}
		}

		// Print the case
		//printf("%d | ", D);
		//for (int i=0; i<D; i++)  {
		//	printf("%d ", Pi.at(i));
		//}
		//printf("| %d \n", maxx);

		// Process the case
		int minutes=maxx, tps=0;


		// If maxx=3, then the best is to wait for 3 minutes so stop splitting after maxx=3
		/*while (maxx>3) {
			
			// Split max value
			if (maxx % 3 == 0) {
				// Split in thirds
				split_thirds(&Pi, imax);
			} else {
				// Split in halves
				split_halves(&Pi, imax);
			}
			
			// Get the new max
			findmax(Pi, &maxx, &imax);
			// Increment the time by 1
			tps ++;

			// Check if leaving everyone + time already spent with special minutes is better than previous best time
			if (maxx+tps < minutes)
				minutes = maxx+tps;
		}*/

		backtrack(Pi, imax, &minutes, tps);

		//printf("| %d minutes\n\n", minutes);


		// Output the case
		if (t<T-1)
			fprintf(fout, "Case #%d: %d\n", t+1, minutes);
		else		
			fprintf(fout, "Case #%d: %d", t+1, minutes);
		
		//printf("Case #%d: %d\n", t+1, minutes);
		fscanf_s(f, "\n");
	}


	fclose(fout);
	fclose(f);

	return 0;
}


