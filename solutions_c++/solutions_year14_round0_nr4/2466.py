#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;


void solve(int &winD, int &win) {
	// input
	int n;
	cin >> n;
	vector<double> na(n, 0.0);
	vector<double> ken(n, 0.0);
	for (int i=0; i<n; i++)
		cin >> na[i];
	for (int i=0; i<n; i++)
		cin >> ken[i];

	sort(na.begin(), na.end());
	sort(ken.begin(), ken.end());
	
	int j=0;
	int i;
	win = n;
	for (i=0; i<n; i++) {
		for ( ; j<n; j++) {
			if (ken[j] > na[i]) {
				--win;
				break;
			}
		}
		j++;

		if (j>=n)
			break;
	}


	//
	winD = n;
	j =0;
	for (int i=0; i<n; i++) {
		if (na[i] < ken[j]) {
			winD--;
		} else {
			j++;
		}
	}
}

int main()
{
	int caseNum;
	cin >> caseNum;

	for (int caseNo=1; caseNo <= caseNum; ++caseNo) {
		int winD, win;
		solve(winD, win);
		cout << "Case #" << caseNo << ": " << winD << ' ' << win << endl;
	}
	return 0;
}
