#include <iostream>
#include <vector>
using namespace std;

int flip(int i, int sol, bool flipped, string& s) {
	while(s[i] != '+' != !flipped) {
		--i;
		if(i < 0) {
			return sol;
		}
	}
	return flip(i, sol+1, !flipped, s);
}

int main() {
	int n;
	cin >> n;
	int t = 1;
	while(t <= n) {
		string s;
		cin >> s;
		cout << "Case #" << t << ": " << flip(s.size()-1, 0, false, s) << endl;
		++t;
	}
}

