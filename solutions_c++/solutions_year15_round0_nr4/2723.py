#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int min(int a, int b) {return (a<b)?a:b;}
int max(int a, int b) {return (a>b)?a:b;}

using namespace std;

unsigned int testNum;

// Richard wins if:
// N >= 7
// H*W is not divisible by N
// an N-ominoe can be constructed that doesn't fit the board in any rotation
// the N-ominoe creates a hole with the wall that's smaller than N (nope (I hope))

int main(int argc, char **argv) {
	ifstream ifile("D-small-attempt1.in");
	FILE *ofile = fopen("out.txt", "w");
	ifile >> testNum;
	for (unsigned i = 0; i < testNum; i++) {
		unsigned n, w, h;
		unsigned nomw, nomh;
		ifile >> n >> w >> h;
		if (n >= 7) goto richard;
		if ((h*w) % n != 0) goto richard;
		nomw = 1;
		nomh = n;
		while (nomh > 0) {
			if ((nomw > w || nomh > h) && (nomw > h || nomh > w)) goto richard;
			if ((nomw == w && nomh+1 == h && nomh > 2) || (nomh == w && nomw+1 == h && nomw > 2) ||
			    (nomw == h && nomh+1 == w && nomh > 2) || (nomh == h && nomw+1 == w && nomw > 2)) goto richard;
			nomh--;
			nomw++;
		}
		fprintf(ofile, "Case #%d: GABRIEL\n", i+1);
		//printf("Case #%d: GABRIEL\n", i+1);
		continue;
		richard:
		fprintf(ofile, "Case #%d: RICHARD\n", i+1);
		//printf("Case #%d: RICHARD\n", i+1);
	}
	ifile.close();
	fclose(ofile);
	return 0;
}
