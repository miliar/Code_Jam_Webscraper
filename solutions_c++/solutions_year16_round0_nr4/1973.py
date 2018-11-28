/*
 * D.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: Yan
 */

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef unsigned long long LL;

int main() {
	FILE *fin = freopen("D-large.in", "r", stdin);
	assert(fin!=NULL);
	FILE *fout = freopen("D-large.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ":";
		int K;
		int C;
		int S;
		cin >> K >> C >> S;
		if (C*S < K) {
			cout << " IMPOSSIBLE" << endl;
			continue;
		}
		int i;
		int j = 0;
		int stop = 0;
		for (i = 0; i <= (K-1)/C; i++) {
			int k;
			LL n = 0;
			LL mult = 1;
			for (k = 0; k < C; k++) {
				n += j * mult;
				mult *= K;
				if (j < K-1) {
					j++;
				}
			}
			cout << " " << n+1;
		}
		cout << endl;
	}
	exit(0);
}


