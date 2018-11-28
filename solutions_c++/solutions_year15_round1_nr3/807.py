#include <fstream>
#include <cassert>
using namespace std;

long long crossProduct(int x1, int y1, int x2, int y2, int x3, int y3) {
	return ((long long) (x2-x1)) * (y3-y1) - ((long long) (x3-x1)) * (y2-y1); 
}

void printAns(int x[], int y[], int n, ofstream &fout) {
	if (n==1) {
		fout << "0" << endl;
		return;
	}

	for (int i=0; i<n; i++) {
		int cutDown = n-1;
		for (int j=0; j<n; j++) {
			if (i != j) {
				int posCount = 0, negCount = 0;
				for (int k=0; k<n; k++) {
					if (k!=i && k!=j) {
						long long pro = crossProduct(x[i], y[i], x[j], y[j], x[k], y[k]);
					    if (pro > 0) 
					    	posCount++;
					    else {
					    	if (pro < 0) 
					    		negCount++;
					    }
					}
				}
				cutDown = min(cutDown, posCount);
				cutDown = min(cutDown, negCount);
			}
		}
		fout << cutDown << endl;
	}
}

int main() {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("pc-small.out");
	assert(fin && fout);

	int test;
	fin >> test;
	for (int count=1; count <= test; count++) {
		int n;
		fin >> n;
		int x[n], y[n];
		for (int i=0; i<n; i++) {
			fin >> x[i] >> y[i];
		}
		fout << "Case #" << count << ":" << endl;
		printAns(x, y, n, fout);
	}
	fin.close();
	fout.close();

	return 0;
}