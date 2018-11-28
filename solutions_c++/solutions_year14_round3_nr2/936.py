#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> trains;

bool isvalid(vector<int>& ind) {
	bool occured[260];
	for (int i = 0; i < 260; ++i)
		occured[i] = false;
	char last;
	for (int i = 0; i < ind.size(); ++i) {
		int t = ind[i];
		for (int j = 0; j < trains[t].size(); ++j) {
			
			char curr = trains[t][j];
			if (!occured[curr]) {
				last = curr;
				occured[curr] = true;
			}
			else if(last != curr)
				return false;
		}
	}
	return true;
}



int main() {
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; ++kase) {
		trains.clear();

		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			string tmp;
			cin >> tmp;
			trains.push_back(tmp);

		}
		vector<int> ind;
		for (int i = 0; i < trains.size(); ++i)
			ind.push_back(i);


		int ans = 0;
		do { 
			// for (int i = 0; i < trains.size(); ++i)
			// 	cout << trains[ind[i]] <<  " ";
			
			if (isvalid(ind)) {
				// cout << "  :: COUNTED" << endl;
				++ans;
			}
			// cout << endl;
		} while ( next_permutation(ind.begin(), ind.end()) );

		printf("Case #%d: %ld\n", kase, ans);
	}
}