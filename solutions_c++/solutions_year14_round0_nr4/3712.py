//============================================================================
// Name        : DeceitfulWar.cpp
// Author      : Rumman
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main(int argc, char ** argv) {
	freopen(argv[1], "r", stdin);
	int t;
	cin >> t;
	for(int ti=0; ti<t; ti++) {
		// get input
		int n, war=0, deceitful_war=0;
		cin >> n;
		float naomi[n], ken[n];
		for(int i=0; i<n; i++) cin >> naomi[i];
		for(int i=0; i<n; i++) cin >> ken[i];

		// sort descending order
		sort(naomi, naomi+n, greater<float>()); sort(ken, ken+n, greater<float>());

		// ** play war
		{
			int kenS = 0;
			int kenE = n-1;

			for(int i=0; i<n; i++) {
				if(naomi[i] > ken[kenS]) {
					war++;
					kenE--;
				} else {
					kenS++;
				}
			}
		}

		// ** play deceitful war
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(naomi[i] > ken[j]) {
					ken[j] = 2;
					deceitful_war++;
					break;
				}
			}
		}

		// Display output
		cout << "Case #" << ti+1 << ": " << deceitful_war << " " << war << endl;
	}
	return 0;
}
