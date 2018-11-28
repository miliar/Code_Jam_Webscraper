#include <fstream>
#include <iostream>
#include <math.h>
using namespace std;

int t;
int d[10000];

int maxd=1;
int r=0x7fffffff;

int main () {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	fin >> t;


	for (int i=0; i<t; i++) {
		int j,k,l,m,n,a,b;
		fin >> m;
		r=0x7fffffff;
		maxd=0;
		cout << "---\n";
		for (j=0; j<m; j++) {
			fin >> n;
			d[j] = n;
			if (maxd<n) maxd=n;
		}

		// after read all data, calculate all cases
		// j: max div num is j.
		r = maxd;
		for (j=2; j<maxd && j<50; j++) {
			a = 0;
			b = 0;
			for (k=0; k<m; k++) {
				b += (d[k]-1)/j;	// total division sum
			}
			cout << "case " << i+1 << "," << j << " - " << b+j << "\n";
			if (r>b+j)
				r=b+j;
		}

		fout << "Case #" << i+1 << ": " << r << "\n";
	}

	return 0;
}
