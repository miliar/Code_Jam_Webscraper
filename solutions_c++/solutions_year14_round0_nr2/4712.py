#include <stdio.h>
#include <string.h>
#include <iostream>
#include <list>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <algorithm>

using namespace std;

double time(double C, double F, double X, double perSec){
	if (X/perSec <= (C/perSec+(X/(perSec+F)))){
		return X/perSec;
	}
	return min<double>(X/perSec, C/perSec + time(C, F, X, perSec+F));
}

int main() {
	int T;
	cin >> T;
	for (int i = 1 ; i <= T ; i++){
		double C, F, X;
		cin >> C >> F >> X;
		printf("Case #%d: %.7f\n", i , time(C, F, X, 2));
//		cout << "Case #" << i << ": " << time(C, F, X, 2) << endl;
	}
}
