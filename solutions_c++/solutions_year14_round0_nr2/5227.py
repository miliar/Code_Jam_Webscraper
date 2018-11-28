//============================================================================
// Name        : Cookie_Clicker_Alpha.cpp
// Author      : alpc92
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int main(void) {
	freopen("out","w",stdout);
	int T;
	double c, f, x;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		cin >> c >> f >> x;
		double curans, minans = 1e300,add=2,curcook=0,cursec=0;
		while (1) {
			curans=cursec+(x-curcook)/add;
			if(curans<minans)minans=curans;
			else break;
			cursec+=c/add;
			add+=f;

		}
		printf("%.7lf\n",minans);
	}
	return 0;
}
