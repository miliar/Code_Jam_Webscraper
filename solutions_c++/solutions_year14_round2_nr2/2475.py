#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	freopen("B-small-attempt0.in","r",stdin); // For reading input.
	freopen("output.txt","w",stdout); // For writing output.
	int t;
	long long res;
	cin >> t;
	for (int i = 0; i < t; i++) {
		res = 0;
		unsigned long long a,b,k;
		cin >> a >> b >> k;
		for (unsigned long long j = 0; j < a; j++) {
			for (unsigned long long m = 0; m < b; m++) {
				if ( (j & m) < k ) {
					res++;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}
