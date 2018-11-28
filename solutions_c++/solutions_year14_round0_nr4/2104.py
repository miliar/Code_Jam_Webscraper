#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int t;
int n;
double nao[1000];
double ken[1000];

int cmp(const void* x, const void* y) {
	return *((double*)x) > *((double*)y) ? 1 : -1;
}

int main() {
	ifstream filein("din.txt");
	ofstream fileout("dout.txt");

	filein >> t;

	for (int i = 1; i <= t; i ++) {
		filein >> n;
		for (int j = 0; j < n; j ++) {
			filein >> nao[j];
		}
		for (int j = 0; j < n; j ++) {
			filein >> ken[j];
		}
		qsort(nao, n, sizeof(double), cmp);
		qsort(ken, n, sizeof(double), cmp);

		//Deceit War
		int kHead = 0, 
			kTail = n - 1, 
			nHead = 0, 
			nTail = n - 1, 
			nScore = 0;
		while (nHead <= nTail) {
			if (nao[nTail] > ken[kTail]) {
				nScore ++;
				kTail --;
				nTail --;
			} else {
				kTail --;
				nHead ++;
			}
		}
		
		fileout <<"Case #"<<i<< ": " << nScore;
		//War
		kHead = 0, 
		kTail = n - 1, 
		nHead = 0, 
		nTail = n - 1, 
		nScore = 0;
		while (kHead <= kTail) {
			if (ken[kTail] < nao[nTail]) {
				nScore ++;
				kHead ++;
				nTail --;
			} else {
				kTail --;
				nTail --;
			}
		}
		fileout << ' ' << nScore << endl;
	}
	return 0;
}