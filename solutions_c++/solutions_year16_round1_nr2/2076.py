#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	long long int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		int n;
		cin >> n;  // read n and then m.
		vector<int> output;
		vector<int> counts;
		for (int j = 0; j < 2501; ++j)
		{
			counts.push_back(0);
		}
		for (int j = 0; j < 2 * n - 1; ++j) {
			for (int k = 0; k < n; ++k) {
				int val;
				cin >> val;
				counts[val - 1] += 1;
			}
		}
		int missing_val = 0;
		for (int j = 0; j < counts.size(); ++j) {
			if (counts[j]%2 == 1)
				output.push_back(j+1);
		}
		
		cout << "Case #" << i << ": ";
		for (int j = 0; j < output.size(); ++j) {
			cout << output[j] << " ";
		}
		cout << endl;
	}
}