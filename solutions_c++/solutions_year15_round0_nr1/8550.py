#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

class StandingOvation {
public:
	void Solve() {
		ifstream fin;
		FILE *fout;
		fout = fopen("standingOvation.out", "w");
		int T;
		fin.open("standingOvation.in");
		fin >> T;

		for (int t = 0; t < T; t++) {
			int sMax;
			string shyness;
			fin >> sMax;
			fin >> shyness;
			int answer = 0;

			int currentTotal = shyness[0] - '0';
			for (int i = 1; i < shyness.length(); i++) {
				int current = shyness[i] - '0';
				if (currentTotal < i && current!=0) {
					int additional = i - currentTotal;
					answer += additional;
					currentTotal += additional;
				}
				currentTotal += current;
			}
			fprintf(fout, "Case #%d: %d\n", t + 1, answer);
		}

		fin.close();
		fclose(fout);
	}

	StandingOvation() {
	}
	~StandingOvation() {
	}
};

int main(int argc, char** argv) {
	StandingOvation so;
	so.Solve();
	return 0;
}