#include "utilities.h"

int main(int argC, char **argV) {
	Initialize(argV[1]);

	int T;
	string line;
	GETLINE(line);
	T = atoi(line.c_str());
	int counter = 0;
	while (counter++ < T) {
		GETLINE(line);
		vector<string> lineVs;
		splitString(line, " ", lineVs);
		double C = atof(lineVs[0].c_str());
		double F = atof(lineVs[1].c_str());
		double X = atof(lineVs[2].c_str());
		double run = 0;
		double remaining = X;
		double rate = 2;

		while (true) {
			double tToX = X / rate;		// running time to make X remaining cookies
			double tToF = C / rate;		// running time to make next factory
			double tToX1 = X / (rate + F);
			if (tToX < tToF + tToX1) {			// if it is quicker to make remaining than make factory
				run += tToX;
				break;
			} else {
				run += tToF;
				rate += F;
			}
		}
		fprintf(out, "Case #%d: %.7f\n", counter, run);
	}
	fclose(in);
	fclose(out);
	return 0;
}