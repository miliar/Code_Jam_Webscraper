#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int lastFalse(const vector<bool>& v) {
	for(int i = v.size()-1; i >= 0; i--) {
		if(!v[i]) return i;
	}
	return -1;
}

void flipTopK(vector<bool>& v, int k) {
	for(int i=0; i<k; i++) {
		v[i] = !v[i];
	}
}

int getMinFlip(string line) {
	int count = 0;
	vector<bool> v;
	for(char ch : line) {
		if('-' == ch) v.push_back(false);
		else v.push_back(true);
	}
	while(true) {
		int idx = lastFalse(v);
		if(idx < 0) return count;
		++count;
		flipTopK(v, idx+1);
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int cas = 1; cas <=t ; cas++) {
		string line;
		cin >> line;
		cout << "Case #" << cas << ": " << getMinFlip(line) << endl;
	}
	return 0;
}
