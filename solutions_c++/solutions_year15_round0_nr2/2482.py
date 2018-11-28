#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

vi pancakes;

const int MAXN = 1005;

int cost(int hi) {	
	int sum = 0;
	for (auto x : pancakes) {
		if (x > hi) {
			sum += x/hi;
			if (x % hi == 0)
				sum--;
		}
	}
	return sum;
}

int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		pancakes.clear();
		
		int D; cin >> D;
		int mas = -1;
		int sol = 1000000000;
		while (D--) {
			int x; cin >> x;
			pancakes.push_back(x);
			mas = max(mas, x);
		}
		
		for (int hi = 1; hi <= mas; hi++) {
			//cout << hi << " -> " << hi << "+" << cost(hi) << endl;
			sol = min(sol, hi + cost(hi));
		}
		
		cout << "Case #" << t << ": " << sol << endl;
	}
}

