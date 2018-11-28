#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)<(b)?(a):(b))

using namespace std;

unsigned int tesztDB;
long long unsigned int elso, utolso, hatar;
bool tulment;

bool palindrom(long long unsigned int szam) {
	unsigned int i, fakt = 0, szamjegy, szamjegy2;
	long long unsigned int tizHatvany = 1;
	while (tizHatvany <= szam) {
		tizHatvany *= 10;
		fakt++;
	}
	tizHatvany /= 10;
	for (i = 0; i < fakt/2; i++) {
		szamjegy = szam-(szam/10)*10;
		szamjegy2 = szam/tizHatvany;
		if (szamjegy != szamjegy2) return false;
		szam -= szamjegy*tizHatvany;
		szam /= 10;
		tizHatvany /= 100;
	}
	return true;
}

bool joParatlan(long long unsigned int szam) {
	long long unsigned int szam2, palSzam, tizHatvany = 1;
	unsigned int hely, szamjegy, fakt = 0;
	while (tizHatvany <= szam) {
		fakt++;
		tizHatvany *= 10;
	}
	if (fakt > 1) {
		fakt *= 2;
		fakt -= 2;
	}
	tizHatvany = 1;
	for (hely = 0; hely < fakt; hely++) tizHatvany *= 10;
	szam2 = szam;
	hely = 0;
	palSzam = szam;
	while (szam2 > 9) {
		szamjegy = szam2-(szam2/10)*10;
		//cout << "|" << szam2 << " " << szam2/10 << endl;
		palSzam += szamjegy*tizHatvany;
		tizHatvany /= 10;
		hely++;
		szam2 /= 10;
	}
	//cout << szam << " -> " << palSzam << endl;
	if (palSzam*palSzam > hatar) {
		tulment = true;
		return false;
	}
	return palindrom(palSzam*palSzam);
}

bool joParos(long long unsigned int szam) {
	long long unsigned int szam2, palSzam, tizHatvany = 1;
	unsigned int hely, szamjegy, fakt = 0;
	while (tizHatvany <= szam) {
		fakt++;
		tizHatvany *= 10;
	}
	fakt *= 2;
	if (fakt > 0) fakt--;
	tizHatvany = 1;
	for (hely = 0; hely < fakt; hely++) tizHatvany *= 10;
	szam2 = szam;
	hely = 0;
	palSzam = szam;
	while (szam2 > 0) {
		szamjegy = szam2-(szam2/10)*10;
		//cout << "|" << szam << " " << palSzam << " " << szam2/10 << endl;
		palSzam += szamjegy*tizHatvany;
		tizHatvany /= 10;
		hely++;
		szam2 /= 10;
	}
	//cout << szam << " -> " << palSzam << endl;
	if (palSzam*palSzam > hatar) {
		tulment = true;
		return false;
	}
	return palindrom(palSzam*palSzam);
}

long long unsigned int megszamol() {
	if (hatar == 0) return 0;
	long long unsigned int i, db = 0, tizHatvany = 1;
	unsigned int faktor = 0, faktor2;
	while (hatar >= tizHatvany) {
		tizHatvany *= 10;
		faktor++;
	}
	faktor2 = faktor;
	faktor2 += 2;
	faktor2 /= 2;
	tizHatvany = 1;
	for (i = 0; i < faktor2; i++) tizHatvany *= 10;
	//cout << hatar << " " << faktor2 << " " << tizHatvany << endl;
	unsigned int utSzamJegy = 0;
	tulment = false;
	for (i = 1; i < tizHatvany; i++) {
		if (i%10 == 0) utSzamJegy = 0;
		else utSzamJegy++;
		if (utSzamJegy != 0 && joParatlan(i)) db++;
		if (tulment) break;
	}
	faktor2 = faktor;
	faktor2--;
	faktor2 /= 2;
	faktor2++;
	tizHatvany = 1;
	for (i = 0; i < faktor2; i++) tizHatvany *= 10;
	//cout << hatar << " " << faktor2 << " " << tizHatvany << endl;
	tulment = false;
	for (i = 1; i < tizHatvany; i++) {
		if (i%10 == 0) utSzamJegy = 0;
		else utSzamJegy++;
		if (utSzamJegy != 0 && joParos(i)) db++;
		if (tulment) break;
	}
	return db;
}

int main(int argc, char **argv) {
	unsigned int i;
	long long unsigned int elsoig, utolsoig;
	ifstream ifile("C-small-attempt0.in");
	FILE *ofile = fopen("out.txt", "w");
	ifile >> tesztDB;
	for (i = 0; i < tesztDB; i++) {
		ifile >> elso >> utolso;
		hatar = elso-1;
		elsoig = megszamol();
		hatar = utolso;
		utolsoig = megszamol();
		//printf("%lli-%lli\n", utolsoig, elsoig);
		fprintf(ofile, "Case #%i: %lli\n", i+1, utolsoig-elsoig);
	}
	ifile.close();
	fclose(ofile);
	return 0;
}
