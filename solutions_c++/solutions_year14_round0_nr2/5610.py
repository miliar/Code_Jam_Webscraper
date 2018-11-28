#include <fstream>
#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

int main() {
	ifstream f("input.txt");
	FILE* g = fopen("output.txt", "wt");
	int t;
	double C, F, X;
	double ans;
	f >> t;
	for(int testCase = 1; testCase <= t; testCase++) {
		f >> C >> F >> X;
		double threshold = (F * X - 2 * C) / (F * C);
		int nrFactories = threshold;
		if(nrFactories > 0) {
			ans = X / (2 + nrFactories * F);
			for(int j = 0; j < nrFactories; j++) {
				ans += C / (2 + j * F);
			}
		}
		else {
			ans = X / 2.0;
		}
		fprintf(g, "Case #%d: %.7lf\n", testCase, ans);
	}
	f.close();
	fclose(g);
	return 0;
}
