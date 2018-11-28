#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main() {
	int T;

	fstream cin("A-small-attempt1.in");
	fstream cout("A-small-attempt1.out");

	cin >> T;

	for(int t=0; t < T; t++) {
		int a1;
		cin >> a1;

		int ar1[4][4];
		for(int i=0; i<4;i++) {
			for(int j=0; j<4;j++) {
				cin >> ar1[i][j];
			}
		}

		int a2;
		cin >> a2;

		int ar2[4][4];
		for(int i=0; i<4;i++) {
			for(int j=0; j<4;j++) {
				cin >> ar2[i][j];
			}
		}

		a1--;
		a2--;
		vector<int> p;
		for(int k=0;k<4;k++){
			for(int i=0;i<4;i++) {
				if (ar1[a1][k] == ar2[a2][i]) p.push_back(ar1[a1][k]);
			}
		}

		cout << "Case #" << t + 1 << ": ";
		if (p.size() == 1) {
			cout << p[0];
		} else if (p.size() > 0) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}

		cout << endl;
	}
	
	return 0;
}