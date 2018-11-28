#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
	ifstream fin ("D-large.in");
	ofstream fout ("D.txt");
	int t;
	fin >> t;
	for (int i = 1; i <= t; i++) {
		int n;
		fin >> n;
		std::vector<double> naomi(n, 0), ken (n, 0);
		for (int j = 0; j < n; j++)
			fin >> naomi[j];
		for (int j = 0; j < n; j++)
			fin >> ken[j];
		sort (naomi.begin(), naomi.end());
		sort (ken.begin(), ken.end());
		// for (int j = 0; j < n; j++)
			// printf("%lf %lf\n", naomi[j], ken[j]);
		
		int nw = 0, ndw = 0, kenix = 0;
		vector <int> flagken(n, 1);
		for (int j = 0; j < n; j++) {
			int nfound  = 1;
			for (int k = kenix; k < n; k++)
				if (ken[k] > naomi[j] && flagken[k]) {
					flagken[k] = 0;
					nfound = 0;
					if (k == kenix)
						kenix++;
					// printf("j = %d, kenix = %d\n", j, kenix);
					break;
				}
		
			if (nfound) {
				// printf("j = %d\n", j);
				nw++;
				flagken[kenix] = 0;
				kenix++;
			}
		}

		flagken.assign (n, 1);
		kenix = 0;
		int kenup = n-1;
		for (int j = 0; j < n; j++) {
			if (ken[kenix] < naomi[j]) {
				ndw++;
				flagken[kenix] = 0;
				kenix++;
			}
			else {
				flagken[kenup] = 0;
				kenup--;
			} 
		}
		// printf("%d %d\n", ndw, nw);
		fout << "Case #" << i << ": " << ndw << " " << nw << "\n";
	}
	return 0;
}