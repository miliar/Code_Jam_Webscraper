/*
 * prob2.cpp
 *
 *  Created on: 12-Apr-2014
 *      Author: Rajan
 */

#include <iostream>
#include <cstdlib>
#include <cstdio>

#define CPM 2

using namespace std;

int main() {

	int T; cin >> T;

	for(int t=0; t<T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;

		cout << "Case #" << t+1 << ": ";
		if(C > X) printf("%.7lf\n", X/CPM);
		else {
			double minTime = X/CPM;
			for(int nf=1; nf<10000; ++nf) {
				double c_rate = CPM, c_time = 0;
				for(int j=0; j<nf; ++j) {
					double time = C/c_rate;
					c_time += time;
					c_rate += F;
				}
				c_time += X/c_rate;
				if(c_time < minTime) minTime = c_time;
			}

			printf("%.7lf\n", minTime);
		}
	}

	return 0;
}

