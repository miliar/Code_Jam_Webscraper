#include <fstream>
#include <cstdlib>

using namespace std;

main () {
	ifstream fin ("B.in");
	FILE *fp = fopen ("B.out", "w");
	int T;
	double C, F, X;
	fin >> T;
	for (int i = 1; i <= T; i++) {
		int c = 0;
		double time = 0;
		fin >> C >> F >> X;
		while (X / (F * c + 2) > X / (F * c + F + 2) + C / (F * c + 2)) {
			time += C / (F * c + 2);
			c++;
		}
		fprintf (fp, "Case #%d: %.7lf\n", i, time + X / (F * c + 2));
	}
	fclose (fp);
}
