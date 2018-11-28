#include <cstdio>
#include <fstream>
#include <iostream>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("a.out");
	int ts;
	in >> ts;
	for (int it = 1; it <= ts; ++it) {
		out << "case #" << it << ": ";
		int n;
		string s;
		in >> n >> s;
		int sum = 0;
		int ans = 0;
		for (int i = 0; i <= n; ++i) {
			if (sum < i) {
				ans += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}
		out << ans << endl;
	}
}