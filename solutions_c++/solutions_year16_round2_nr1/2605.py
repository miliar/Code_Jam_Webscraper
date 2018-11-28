#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ifstream archEnt;
	ofstream archSal;

	archEnt.open("entrada.txt");
	archSal.open("salida.out");

	int numVeces = 0;

	archEnt >> numVeces;

	for (int i = 0; i < numVeces; ++i) {
		string S = "";
		int contZ = 0, contW = 0, contX = 0, contU = 0, contG = 0, contN = 0, contS = 0, contF = 0, contH = 0, contO = 0;
		
		archEnt >> S;

		for (int j = 0; j < S.size(); ++j) {
			if (S[j] == 'Z') ++contZ;
			else if (S[j] == 'W') ++contW;
			else if (S[j] == 'X') ++contX;
			else if (S[j] == 'U') ++contU;
			else if (S[j] == 'G') ++contG;
			else if (S[j] == 'N') ++contN;
			else if (S[j] == 'S') ++contS;
			else if (S[j] == 'F') ++contF;
			else if (S[j] == 'H') ++contH;
			else if (S[j] == 'O') ++contO;
		}
		contO -= (contU + contW + contZ);
		contS -= contX;
		contF -= contU;
		contH -= contG;
		contN = (contN - (contO + contS)) / 2;

		archSal << "Case #" << i + 1 << ": ";
		for (int j = 0; j < contZ; ++j)
			archSal << 0;
		for (int j = 0; j < contO; ++j)
			archSal << 1;
		for (int j = 0; j < contW; ++j)
			archSal << 2;
		for (int j = 0; j < contH; ++j)
			archSal << 3;
		for (int j = 0; j < contU; ++j)
			archSal << 4;
		for (int j = 0; j < contF; ++j)
			archSal << 5;
		for (int j = 0; j < contX; ++j)
			archSal << 6;
		for (int j = 0; j < contS; ++j)
			archSal << 7;
		for (int j = 0; j < contG; ++j)
			archSal << 8;
		for (int j = 0; j < contN; ++j)
			archSal << 9;

		archSal << '\n';
		}

	archSal.close();
	archEnt.close();


	return 0;
}