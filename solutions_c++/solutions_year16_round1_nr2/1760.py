#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include "stdio.h"

using namespace std;
int n;
int d[100][50];
int valcount[3000];
int main() {
	int t;
	cin >> t;


	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> n;
		for (int i = 0; i < 3000; ++i)
			valcount[i] = 0;
		for (int i = 0; i < 2*n-1; ++i)
			for (int j = 0; j < n; ++j) {
					cin >> d[i][j];
					valcount[d[i][j]] ++;
			}
		int l[200];
		int lpt = 0;
		for (int i = 0; i < 3000; ++i)
			if (valcount[i] % 2 > 0)
				l[lpt++] = i;
		//sort(l, l + n);

		cout << "Case #" << tcount << ": ";
		for (int i = 0; i < n; ++i)
			cout << l[i] << " ";
		cout << endl;
	}

	return 0;
}