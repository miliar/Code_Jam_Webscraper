/*
 * B.cpp
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
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin!=NULL);
	FILE *fout = freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		string S;
		cin >> S;
		S = S + '+';
		int n = S.length();
		int i;
		int count = 0;
		for (i = 1; i < n; i++) {
			if (S[i] != S[i-1]) {
				count++;
			}
		}
		cout << count << endl;
	}
	exit(0);
}


