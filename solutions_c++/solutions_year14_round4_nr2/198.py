#include <iostream>
#include <algorithm>
using namespace std;

long long cases, nums;
long long original[1000], sorted[1000], temp[1000];

int main() {
	cin>>cases;
	for (long long c = 1; c <= cases; c++) {
		cin>>nums;
		
		for (long long i = 0; i < nums; i++) {
			cin>>original[i];
		}

		int l = 0, r = nums-1;

		int swaps = 0;
		for (int i = 0; i < nums; i++) {
			// find smallest
			int sval = (1<<30);
			int si = -1;
			for (int j = l; j <= r; j++) {
				if (original[j] < sval) {
					sval = original[j];
					si = j;
				}
			}

			if (si - l > r - si) {
				// move to right
				for (int j = si; j < r; j++) {
					original[j] = original[j+1];
					swaps++;
				}
				original[r] = sval;
				r--;
			} else {
				// move to the left
				for (int j = si; j > l; j--) {
					original[j] = original[j-1];
					swaps++;
				}
				original[l] = sval;
				l++;
			}
		}

		cout<<"Case #"<<c<<": "<<swaps<<"\n";
	}
}