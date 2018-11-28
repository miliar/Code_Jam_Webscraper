#include<iostream>
#include<vector>
#include<string>

using namespace std;

int calcFlip(string s){
	vector<int> cakes(s.size(), 0);
	for (int i = 0; i < (int) s.size(); i++) {
		if (s[i] == '-') {
			cakes[i] = 0;
		}
		else {
			cakes[i] = 1;
		}
	}
	int flip = 0;
	for (int i = s.size() - 1; i >= 0; i--) {
		if ((cakes[i] + flip) % 2 == 0) {
			flip++;
		}
	}
	return flip;
}

int main () {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		string s; cin >> s;
		cout << "Case #" << i << ": " << calcFlip(s) << endl;
	}
}
