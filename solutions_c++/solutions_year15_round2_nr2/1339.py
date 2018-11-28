#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
using namespace std;

int unhappiness(int r, int c, int n, int occup[]) {
	int count = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (occup[i*c+j] && i < r-1 && occup[(i+1)*c + j] != 0) count++;
			if (occup[i*c+j] && j < c-1 && occup[i*c + j+1] != 0) count++;
		}
	}
	return count;
}

int answer(int r, int c, int n) {
	int occup[r*c];
	for (int i = 0; i < r*c-n; i++) {
		occup[i] = 0;
	}
	for(int i = r*c-n; i< r*c; i++)  {
		occup[i] = 1;
	}
	int mn = unhappiness(r,c,n, occup);
	while(next_permutation(occup, occup+r*c)) {
		//cout << "perm ";
		//for (int i = 0; i < r*c; i++) cout << occup[i] << " ";
		//cout << endl;
		mn = min(mn, unhappiness(r, c, n, occup));
	}
	return mn;
}

int main()
{
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int r,c,n;
		cin >> r >> c >> n;
		cout << "Case #" << _t << ": " << answer(r,c,n) << endl;
	}
    return 0;
}
