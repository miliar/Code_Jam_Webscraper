#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)<(b)?(a):(b))

using namespace std;

unsigned int tesztDB, **fuvek, hossz, szel;
bool **jo;

bool leJo(unsigned int y, unsigned int x, unsigned int szam) {
	if (y >= hossz) return true;
	if (fuvek[y][x] != szam) return false;
	return leJo(y+1, x, szam);
}
void leBejelol(unsigned int x) {
	for (unsigned int i = 0; i < hossz; i++) jo[i][x] = true;
}
bool jobbraJo(unsigned int y, unsigned int x, unsigned int szam) {
	if (x >= szel) return true;
	if (fuvek[y][x] != szam) return false;
	return jobbraJo(y, x+1, szam);
}
void jobbraBejelol(unsigned int y) {
	for (unsigned int i = 0; i < szel; i++) jo[y][i] = true;
}
bool novel(unsigned int szam) {
	for (unsigned int i = 0; i < hossz; i++) {
		for (unsigned int j = 0; j < szel; j++) {
			if (fuvek[i][j] == szam) {
				if (jo[i][j]) fuvek[i][j]++;
				else return false;
			}
		}
	}
	return true;
}

int main(int argc, char **argv) {
	unsigned int i, j, k;
	ifstream ifile("B-large.in");
	FILE *ofile = fopen("out.txt", "w");
	ifile >> tesztDB;
	for (i = 0; i < tesztDB; i++) {
		ifile >> hossz >> szel;
		fuvek = new unsigned int*[hossz];
		jo = new bool*[hossz];
		for (j = 0; j < hossz; j++) {
			fuvek[j] = new unsigned int[szel];
			jo[j] = new bool[szel];
			for (k = 0; k < szel; k++) {
				ifile >> fuvek[j][k];
				jo[j][k] = false;
			}
		}
		/*for (j = 0; j < hossz; j++) {
			for (k = 0; k < szel; k++) printf("%i ", fuvek[j][k]);printf("\n");
		}printf("\n");*/
		fprintf(ofile, "Case #%i: ", i+1);
		for (j = 1; j <= 100; j++) {
			for (k = 0; k < szel; k++) {
				if (leJo(0, k, j)) leBejelol(k);
			}
			for (k = 0; k < hossz; k++) {
				if (jobbraJo(k, 0, j)) jobbraBejelol(k);
			}
			if (!novel(j)) {
				fprintf(ofile, "NO\n");
				break;
			}
			if (j == 100) fprintf(ofile, "YES\n");
		}
		for (j = 0; j < hossz; j++) {
			delete[] fuvek[j];
			delete[] jo[j];
		}
		delete[] fuvek;
		delete[] jo;
	}
	ifile.close();
	fclose(ofile);
	return 0;
}
