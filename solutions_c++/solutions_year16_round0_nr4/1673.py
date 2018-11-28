#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;

ull pow(int a, int b){
	ull res = 1;
	for (int i = 0; i < b; ++i) {
		res *= a;
	}
	return res;
}

int main() {
	int t; cin >> t;
	for (int a0 = 0; a0 < t; ++a0) {
		int k, c, s; cin >> k >> c >> s;
		vector<ull> pos;
		for (int i = 0; i < k; ++i) {
			pos.push_back(1 + i * pow(k, c - 1));
		}
		cout << "Case #" << (a0 + 1) << ":";
		for (auto x : pos) {
			cout << " " << x;
		}
		cout << endl;
	}
	
	return 0;
}