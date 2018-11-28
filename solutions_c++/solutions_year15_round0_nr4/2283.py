// ConsoleApplication2.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

#define GABRIEL 0
#define RICHARD 1

int main() {

	FILE *f, *fout;
	fopen_s(&f, "data4/D-small-attempt0.in", "r");
	fopen_s(&fout, "data4/D-small-attempt0.out", "w");

	int T=0, R=0, X=0, C=0;
	int Smax=0;
	vector<int> inv;
	char tmp=0;
	int winner=GABRIEL;

	fscanf_s(f, "%d\n", &T);

	for (int t=0; t<T; t++) {
		// Read the case
		for (int c=0; c<Smax+1; c++) {
			fscanf_s(f, "%d %d %d\n", &X, &R, &C);		
		}

		// Print the case
		//printf("%d %d %d\n", X, R, C);
		//for (int i=0; i<Smax+1; i++)  {
		//	printf("%d", inv.at(i));
		//}
		//printf("\n");

		// Process the case

		// Richard wins if the size of the board is not a multiple of the X-omino size 
		// or not wide/high enough

		// Get the maximum width X-omino we can do with X
		int maxwidth = (X+1)/2;
		if ( ( R*C % X != 0) || ( maxwidth>R ) || ( maxwidth>C ) ) {
			winner = RICHARD;
		} else {
			// If 1-omino, 2-omino or 3-omino Gabriel wins
			if ( X<=3 )
				winner = GABRIEL;
			else {

				// Small case
				if (X==4) {
					if ( C==2 || R==2 )
						winner = RICHARD;
					else
						winner = GABRIEL;
				} 

				// For X>=7 we can have X-omino with a hole in it, making it impossible to fill
				if (X>=7)
					winner = RICHARD;

				if (X==5 || X==6) {
					if (maxwidth==R || maxwidth==C)
						winner = RICHARD;
					else
						winner = GABRIEL;
				}
			}
		}
		

		// Print output
		char res[200];
		(winner == 0 ? sprintf_s(res, "GABRIEL") : sprintf_s(res, "RICHARD")) ;
		if (t<T-1)
			fprintf(fout, "Case #%d: %s\n", t+1, res);
		else		
			fprintf(fout, "Case #%d: %s", t+1, res);

		//printf("Case #%d: %s\n", t+1, res);
	}


	fclose(fout);
	fclose(f);

	return 0;
}