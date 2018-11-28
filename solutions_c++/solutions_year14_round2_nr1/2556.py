#include <iostream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	int T, N;
	string list[110];
	char model[110], nmodel[110];
	int count[110][110], ncount[110], dif, ndif;
	bool posible;
	cin >> T;

	for (int t=1 ; t<=T ; t++) {
		cin >> N;
		posible = true;
		for (int i=0 ; i<N ; i++)
			cin >> list[i];

		model[0] = list[0][0];
		count[0][0] = 0;
		dif = 0;
		for (int i=0 ; i<list[0].length() ; i++) {
			if (list[0][i] != model[dif]) {
				model[dif+1] = list[0][i];
				count[0][dif+1] = 1;
				dif++;
			} else count[0][dif]++;
		}
		dif++;

		for (int n=1 ; n<N ; n++) {
			nmodel[0] = list[n][0];
			ncount[0] = 0;
			ndif = 0;
			for (int i=0 ; i<list[n].length() ; i++) {
				if (list[n][i] != nmodel[ndif]) {
					nmodel[ndif+1] = list[n][i];
					ncount[ndif+1] = 1;
					ndif++;
				} else ncount[ndif]++;
			}
			ndif++;

			if (dif != ndif) {
				posible = false;
			} else {
				for (int i=0 ; posible && i<dif ; i++)
					posible = (model[i] == nmodel[i]);
			}

			if (!posible) break;

			for (int i=0 ; i<dif ; i++)
				count[n][i] = ncount[i];
		}

		cout << "Case #" << t << ": ";
		if (posible) {
			int minplays = 0;
			for (int i=0 ; i<dif ; i++) {
				int sum = 0;
				for (int n=0 ; n<N ; n++)
					sum += count[n][i];
				sum /= N;
				int a=0, b=0;
				for (int n=0 ; n<N ; n++) {
					a += abs(sum-count[n][i]);
					b += abs(sum+1-count[n][i]);
				}
				minplays += min(a,b);
			}
			cout << minplays << endl;
		} else {
			cout << "Fegla Won" << endl;
		}
	}

	return 0;
}
