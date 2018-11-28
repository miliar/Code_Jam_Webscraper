#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int cn; 
	ifstream inf("B-large.in");
	ofstream outf("B-large.out");

	inf>>cn;
	for(int i=0; i <cn ; i++) {
		int m, n;
		int **lawn;
		int *rmax, *cmax;
		inf>>m>>n;

		rmax = new int [m];
		cmax = new int [n];
		lawn = new int *[m];

		for(int j=0; j<m; j++) {
			lawn[j] = new int [n];
			rmax[j] = 0;
		}
		for(int j=0; j<n; j++) {
			cmax[j] = 0;
		}
		for(int j=0; j<m; j++) {
			for(int k=0; k<n; k++) {
				inf>>lawn[j][k];
				rmax[j] = max(rmax[j], lawn[j][k]);
				cmax[k] = max(cmax[k], lawn[j][k]);
			}
		}

		bool ans = true;
		for(int j=0; j<m; j++) {
			for(int k=0; k<n; k++) {
				if(lawn[j][k] < rmax[j] && lawn[j][k] < cmax[k]) {
					ans = false;
					break;
				}
			}
			if(!ans) {
				break;
			}
		}
		outf<<"Case #"<<i+1<<": "<<((ans) ? "YES" : "NO")<<endl;
	}
	return 0;
}
