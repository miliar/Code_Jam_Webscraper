#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int nCases, cDiners, diners[1001];

int calcMin() {
	int min = 1000;
	for(int t=1; t<=1000; t++) {
		int c = 0;
		for (int i=t; i<=1000; i++) {
			int n = i/t - 1;
			if (i % t > 0) n++;
			c += n*diners[i];
		}
		if (min > c+t) min = c+t;
	}
	return min;
}

int main() {
	int in, min;
	cin >> nCases;
	for (int i=0; i<nCases; i++) {
		for (int j=0; j<1001; j++) diners[j]=0;
		cin >> cDiners;
		for (int j=0; j<cDiners; j++) {
			cin >> in;
			diners[in]++;
		}
		cout << "Case #" << i+1 << ": " << calcMin() << endl; 
	}
	return 0;
}