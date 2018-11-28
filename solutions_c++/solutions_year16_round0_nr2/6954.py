#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool ready(const vector<int> &a) {
	for (int i = 0; i < a.size(); i++) {
		if (a[i] == 0) {
			return false;
		}
	}
	return true;
}

int solve(string &s) {
	vector<int> a(s.size());
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '+') {
			a[i] = 1;
		} else {
			a[i] = 0;
		}
	}
	int k = 0;
	while (!ready(a)) {
		int first = a[0];
		int i = 0;
		while (i < a.size() && a[i] == first) {
			a[i] = (first + 1) % 2;
			i++;
		}
		k++;
	}
	return k;
	
}

int main() {
	ifstream f("C:\\Users\\yevhe_000\\Desktop\\input.txt");
	ofstream g("C:\\Users\\yevhe_000\\Desktop\\output.txt");
	int n;
	f >> n;
	string s;
	for (int i = 0; i < n; i++) {
		f >> s;
		g << "Case #" << i+1 << ": " << solve(s) << endl;
	}
	f.close();
	g.close();
	return 0;
}