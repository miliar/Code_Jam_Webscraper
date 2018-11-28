#include <limits.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
	int cases;
	cin >> cases;
	vector<int> diners(cases);
	vector<vector<int> > pancakes(cases);
	for (int i=0; i<cases; ++i) {
		cin >> diners[i];
		for (int j=0; j<diners[i]; ++j) {
			int pancake;
			cin >> pancake;
			pancakes[i].push_back(pancake);
		}
	}

	for (int i=0; i<cases; ++i) {
		int n = diners[i];
		vector<int>& a = pancakes[i];

		sort(a.begin(), a.end());
		int answer = INT_MAX;
		for (int k=1; k<=a[a.size()-1]; ++k) {
			int cuts_needed = 0;
			for (const int& height : a) {
				if (height <= k)
					continue;
				cuts_needed += ((height + k - 1) / k ) -1; // ceiling - 1
			}
			if (answer > cuts_needed + k)
				answer = cuts_needed + k;
		}
		cout << "Case #" << i+1 << ": " << answer << endl;
	}

	return 1;
}