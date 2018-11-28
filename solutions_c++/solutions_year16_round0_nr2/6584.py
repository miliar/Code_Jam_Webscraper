#include <fstream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

#define up(c) ((c) == '+')

ifstream cin("input.txt");
ofstream cout("output.txt");

int process(string s) {
	int a[101], b[101];
	memset(a, 0, sizeof a);
	memset(b, 0, sizeof b);
	if (up(s[0])) a[0] = 0, b[0] = 1;
	else a[0] = 1, b[0] = 0;
	for (int i = 1; i != s.length(); ++i) {
		if (up(s[i])) {
			a[i] = min(a[i - 1], b[i - 1] + 1);
			b[i] = min(a[i - 1] + 1, b[i - 1] + 2);
		}
		else {
			a[i] = min(a[i - 1] + 2, b[i - 1] + 1);
			b[i] = min(a[i - 1] + 1, b[i - 1]);
		}
	}
	return a[s.length() - 1];
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i != t; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": " << process(s) << endl;
	}
	return 0;
}