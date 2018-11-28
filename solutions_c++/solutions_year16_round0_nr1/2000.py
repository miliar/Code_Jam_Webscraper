/*
 * A.cpp
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
typedef long long LL;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin!=NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int n = 0;
		int asdf;
		int s;
		int N;
		cin >> N;
		if (N == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int d[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int nd = 0;
		while (nd < 10) {
			n += N;
			asdf = n;
			while (asdf > 0) {
				s = (asdf % 10);
				if (!d[s]) {
					d[s] = 1;
					nd++;
				}
				asdf = (asdf / 10);
			}
		}
		cout << n << endl;
	}
	exit(0);
}

