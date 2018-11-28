#include <bits/stdc++.h>
using namespace std;

// true is +



void flip(vector<bool>& v, unsigned int length) {
	reverse(v.begin(), v.begin() + length);
	for (unsigned int i = 0; i < length; i++) {
		v[i] = !v[i];
	}
}

int solve(vector<bool>& inp) {
	while (inp.back()) {
		inp.pop_back();
	}
	if (!inp.size()) {
		return 0;
	}
	if (inp[0]) {
		// flip to convert start to -!
		unsigned int i = 0;
		while (i < inp.size() && inp[i]) {
			i++;
		}
		flip(inp, i);
	} else {
		// flip everything to get rid of -
		flip(inp, inp.size());
	}

	// for (bool b : inp) {
	// 	cerr << b << " ";
	// }
	// cerr << endl;
	return 1 + solve(inp);
}


int main() {
	int n;
	int j = 1;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string temp;
		cin >> temp;
		vector<bool> inp;
		for (char c : temp) {
			inp.push_back(c == '+');
			// cerr << inp.back() << " ";
		}
		// cerr << endl;
		cout << "Case #" << j++ << ": " << solve(inp) << endl;
	}
}
