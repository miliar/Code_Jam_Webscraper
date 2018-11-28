#include <iostream>
#include <cmath>
#include <stdio.h>
#include <vector>

using namespace std;

int main() {
	int nc;
	cin >> nc;
	
	for (int cc = 0; cc < nc; cc++) {
		double C, F, X;
		cin >> C >> F >> X;
		vector<double> tblTTB;
		vector<double> tblTTL;
		
		// C: Cost of Farm
		// F: Rate Increase
		// X: Goal.
		double R   = 2;
		int    nF  = 0;
		double TTB = 0;
		double TTL = X / R;
		
		double minCost = TTB + TTL;
		
		while (TTB < X) {
			TTB += C / R;
			nF++;
			R = 2 + F * nF;
			TTL = X / R;
			
			if (minCost < TTB + TTL) {
				break;
			}
			else {
				minCost = TTB + TTL;
			}
		}
		
		printf("Case #%d: %.7f\n", cc + 1, minCost);
	}

	return 0;
}