#include <iostream>
#include <fstream>
#include <string>

using namespace std;

long change(string s) {
	long ans = 0;
	for (int i=0; i<s.size(); i++) {
		ans = ans * 10 + int(s[i]) - 48;
	}
	return ans;
}

int gcd(long a, long b) {
	int t;
	if (a < b) {
		t = a; a = b; b = t;
	}
	if (a % b == 0) {
		return b;
	}
	a = a % b;
	return gcd (a, b);
}

int main() {
	ifstream input("A-small-attempt0.in");
	ofstream output("ans.out");
	int t;
	long a, b;
	string s, s1, s2;
	input >> t;
	for (int ii=0; ii<t; ii++) {
		input >> s;
		for (int j=0; j<s.size(); j++) {
			if (s[j] == '/') {
				s1 = s.substr(0, j);
				s2 = s.substr(j+1, s.size()-j-1);
				break;
			}
		}
		a = change(s1);
		b = change(s2);
		int c = gcd(a,b);
		a = a/c;
		b = b/c;

		int flag = 0;
		if (a <= b) {
			long x = 1;
			for (int i=0; i<40; i++) {
				x = x * 2;
				if (x % b == 0) {
					int count = 0;
					while (a < x) {
						x /= 2;
						count++;
					}
					output << "Case #" << ii+1 << ": " << count << endl;
					flag = 1;
					break;
				}
			}
		}

		if (flag == 0)
			output << "Case #" << ii+1 << ": " << "impossible" << endl;
	}
}