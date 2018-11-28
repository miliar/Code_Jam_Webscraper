#include "utilities.h"

#define TEST(x) 1/((double)(1 << x))

bool testForPowerTwo(int x) {
	int n = 0;
	int ref = x;
	while (x > 0) {
		x >>=1;
		n++;
	}
	return (ref == (1 << (n - 1)));
}

int main(int argC, char **argV) {
	Initialize(argV[1]);

	int T;
	string line;
	GETLINE(line);
	T = atoi(line.c_str());
	int counter = 0;
	while (counter++ < T) {
		fprintf(out, "Case #%d: ", counter);
		bool impossible = false;
		GETLINE(line);
		int x=0;
		int y=0;
		sscanf(line.c_str(), "%d/%d", &x, &y);
		if (!testForPowerTwo(y)) {
			fprintf(out, "impossible\n");
			continue;
		}
		double testCase = (double) x / (double) y;
		int i = 1;
		for (i = 1; i <= 40; i++) {
			double testValue = TEST(i);
			if (testCase >= testValue) {
				break;
			}
		}
		if (i > 40) {
			fprintf(out, "impossible\n");
		} else {
			fprintf(out, "%d\n", i);
		}
	}
	fclose(in);
	fclose(out);
	return 0;
}