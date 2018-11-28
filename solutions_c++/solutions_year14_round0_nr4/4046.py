#include <fstream>
#include <bits/stdc++.h>
#include<cstdlib>
#include<cstdio>
#include <iostream>
#include <iomanip>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int normalGameWar(vector<double> N, vector<double> K) {
	int Temp = 0;
	for (unsigned int i = 0; i < N.size(); i++) {
		for (unsigned int j = 0; j < K.size(); j++) {

			if (N[i] < K[j]) {
				K.erase(K.begin() + j);
				break;
			}
			if (j == K.size() - 1)
				Temp++;
		}
	}
	return Temp;
}

int deceitfulGameWar(vector<double> N, vector<double> K) {
	int value = 0;
	for (int i = N.size() - 1; i >= 0; i--) {
		if (N[i] > K[K.size() - 1]) {
			K.erase(K.begin() + (K.size() - 1));
			N.erase(N.begin() + i);
			value++;
		} else {
			if (N[0] < K[K.size() - 1]) {
				K.erase(K.begin() + (K.size() - 1));
				N.erase(N.begin());
			}
		}
	}
	return K.size() + value;
}
int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int nTestCases;
	cin >> nTestCases;
	for (int i = 1; i <= nTestCases; i++) {
		int nOfWeights;
		cin >> nOfWeights;
		vector<double> n , k;
		for (int j = 0; j < nOfWeights; j++) {
			double m;
			cin >> m;
			n.push_back(m);
		}

		for (int j = 0; j < nOfWeights; j++) {
			double m;
			cin >> m;
			k.push_back(m);
		}
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());
		int y = normalGameWar(n, k);
		int z = deceitfulGameWar(n, k);
		cout << "Case #" << i << ": " << z << " " << y << endl;
	}
	return 0;
}
