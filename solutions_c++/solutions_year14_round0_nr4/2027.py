#include<fstream>
#include<cstdlib>
using namespace std;

int compar(const void *first, const void *second) {
	double f = *(double *)first;
	double s = *(double *)second;
	return (f > s) ? 1 : (f == s) ? 0 : -1;
}

double naomi[1000], ken[1000];

int main() {
	int t, it, n, i, j, scoreWar, scoreDeceitfulWar;
	ifstream fin("input.in");
	ofstream fout("output.out");
	fin >> t;
	for(it = 1; it <= t; it++) {
		scoreDeceitfulWar = scoreWar = 0;
		fin >> n;
		for(i = 0; i < n; i++) fin >> naomi[i];
		for(i = 0; i < n; i++) fin >> ken[i];

		qsort(naomi, n, sizeof(double), compar);
		qsort(ken, n, sizeof(double), compar);

		i = j = 0;
		while(i < n) {
			if(naomi[i] > ken[j]) {
				i++;
				j++;
				scoreDeceitfulWar++;
			} else {
				i++;
			}
		}

		i = j = n-1;
		while(i >= 0) {
			if(naomi[i] > ken[j]) {
				i--;
				scoreWar++;
			} else {
				i--;
				j--;
			}
		}

		fout << "Case #" << it << ": " << scoreDeceitfulWar << " " << scoreWar << "\n";
	}
	return 0;
}
