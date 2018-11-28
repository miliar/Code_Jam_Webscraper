#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void print(int *res, int n) {
	ofstream file("a.out");
	for (int i = 0; i < n; i++) {
		file << "Case #" << i + 1 << ": " << res[i];
		file << endl;
	}
	file.close();

}
bool flip(string &s) {
	int ii = 0;
	bool found = false;
	for (int i = s.size() - 1;i >= 0; i--) {
		if (s[i] == '-') {
			ii = i;
			found = true;
			break;
		}
	}
	if (!found) return true;

	for (int i = 0; i < ii+1; i++) {
		if (s[i] == '-') {
			s[i] = '+';
		}
		else {
			s[i] = '-';
		}
	}
	return false;
}
int main() {
	int n, *res, c;
	ifstream file("i.in");
	string s;
	file >> n;
	res = new int[n];
	for (int i = 0; i < n; i++) {
		file >> s;
		c = 0;
		while (!flip(s)) {
			c++;
		}
		res[i] = c;
	}
	print(res, n);
	file.close();
	return 0;
}