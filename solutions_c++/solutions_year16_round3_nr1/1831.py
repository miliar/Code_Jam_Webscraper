#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

int maximum(vector<int> p) {
	int max  = 0;
	for(int i = 1; i < (int)p.size(); i++) {
		if(p.at(i) > p.at(max))
			max = i;
	}
	return max;
}

int todo(vector<int> p) {
	int count = 0;
	for(int i = 0; i < (int)p.size(); i++)
		count += p.at(i);
	return count;
}

void solve(vector<int> p){
	while(42) {
		if(todo(p) <= 2) {
			int max = maximum(p);
			cout << (char)('A' + max);
			p.at(max)--;
			max = maximum(p);
			cout << (char)('A' + max);
			break;
		}
		int max = maximum(p);
		int val = p.at(max);
		cout << (char)('A' + max);
		p.at(max)--;

		if(p.at(maximum(p)) > (todo(p) / 2)) {
			max = maximum(p);
			cout << (char)('A' + max);
			p.at(max)--;
		}
		cout << " ";
	}
}

int main() {
	int t, n;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		vector<int> p;
		for(int j = 0; j < n; j++) {
			int x;
			cin >> x;
			p.push_back(x);
		}
		cout << "Case #" << (i + 1) << ": ";
		solve(p);
		cout << endl;
	}

	return EXIT_SUCCESS;
}
