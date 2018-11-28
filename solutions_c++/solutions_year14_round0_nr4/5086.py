//============================================================================
// Name        : Deceitful.cpp
// Author      : alpc92
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(void) {
	int T;
	freopen("out","w",stdout);
	cin >> T;
	for (int t = 1; t <= T; ++t) {

		int n;
		cin >> n;
		vector<double> N, K, tK;
		N.resize(n);
		K.resize(n);
		for (int i(0); i < n; ++i)
			cin >> N[i];
		sort(N.begin(), N.end());

		for (int i(0); i < n; ++i)
			cin >> K[i];
		sort(K.begin(), K.end());

		int sw = 0, sd = 0;
		tK = K;
		for (int i = 0; i < n; ++i) {
			bool win = 1;
			for (vector<double>::iterator it = K.begin(); it != K.end(); ++it) {
				if (*it > N[i]) {
					K.erase(it);
					win = 0;
					break;
				}
			}
			if (win) {
				K.erase(K.begin());
				++sw;
			}
		}
		K = tK;
		for (int i = 0; i < n; ++i) {
			//cout<<N[i]<<" ";
			bool win = 1;
			for (vector<double>::iterator it = K.begin(); it != K.end(); ++it) {
				if (*it > N[i]) {
					win = 0;
					break;
				}
			}
			if (win) {
				//cout<<*K.begin()<<endl;
				K.erase(K.begin());
				++sd;
			} else {
				if (N[i] >= *K.begin()) {
					//cout<<*K.begin()<<endl;
					K.erase(K.begin());
					++sd;
				}else {

					//cout<<K.back()<<endl;
					K.pop_back();
				}
			}
		}
		printf("Case #%d: %d %d\n", t, sd, sw);
	}
	return 0;
}
