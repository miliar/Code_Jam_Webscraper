#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

int flip(bool* m, int falsecount) {
	int i;
	int t = -1;
	for (i = 0; i < falsecount + 1; i++) {
		if (m[i] == true) {
			m[i] = false;
			t = i;
		} else {
			m[i] = true;
		}
	}

	return t;

}

int main() {
	int test;
	cin >> test;

	int n;
	string abc;
	getline(cin, abc);
	for (n = 0; n < test; n++) {
		getline(cin, abc);
		cout<<"Case #"<<(n + 1)<<": ";
		int t = abc.length();
		bool * d = (bool *) malloc (t * sizeof(bool));
		int i;
		int falsecount = -1;
		for (i = 0; i < t; i++) {
			char m = abc.at(i);
			if (m == '+') {
				d[i] = true;
			} else {
				d[i] = false;
				falsecount = i;
			}
		}
		int s = 0;
		while (falsecount != -1) {
			falsecount = flip(d, falsecount);
			s++;
		}
		cout << s <<endl;;
	}

}


