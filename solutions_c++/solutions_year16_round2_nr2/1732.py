#include <iostream>
#include <climits>
#include <cmath>
using namespace std;

int mind;
int minc;
int minj;
string aa, bb;

void solve (string a, string b, int i) {
	if (i == a.length()) {
		int diff = abs(stoi(a) - stoi(b));
		if (diff < mind) {
			mind = diff;
			aa = a;
			bb = b;
		} else if (diff == mind) {
			if (stoi(a) < stoi(aa)) {
				aa = a;
				bb = b;
			} else if (stoi(a) == stoi(aa)) {
				if (stoi(b) < stoi(bb)) {
					aa = a;
					bb = b;
				}
			}
		}
		return;
	}
	if (a[i] != '?' && b[i] != '?') {
		solve (a, b, i+1);
	} else if (a[i] == '?') {
		for (int j = 0; j < 10; j++) {
			a[i] = (char)('0'+j);
			if (b[i] == '?') {
				solve (a, b, i);
			} else {
				solve (a, b, i+1);
			}
		}
	} else if (b[i] == '?') {
		for (int j = 0; j < 10; j++) {
			b[i] = (char)('0'+j);
			solve (a, b, i+1);
		}
	}
}

int main () {
	int t;
	cin >> t;
	for (int casei = 1; casei <= t; casei++) {
		string a, b;
		cin >> a >> b;
		int len = a.length();
		mind = INT_MAX;
		minc = INT_MAX;
		minj = INT_MAX;
		aa=""; bb="";
		solve (a, b, 0);
		cout << "Case #" << casei << ": " << aa << " " << bb << endl;
	}
	return 0;
}