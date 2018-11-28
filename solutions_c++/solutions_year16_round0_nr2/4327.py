#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main() {
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	long T;
	in >> T;
	
	string s;
	int plus;
	int ans;
	int n;
	for (long i = 0; i < T; i++) {
		in >> s;
		plus = 0;
		ans = 0;

		n = s.size();
		for (int j = n - 1; j >= 0; j--) {
			if (s[j] == '-') {
				break;
			}
			plus++;
		}
		if (plus == n) {
			out << "Case #" << i + 1 << ": " << 0 << '\n';
			continue;
		}
		for (int j = 0; j < n - plus - 1; j++) {
			if (s[j] != s[j + 1]) {
				ans++;
			}
		}
		out << "Case #" << i + 1 << ": " << ans+1 << '\n';
	}

	in.close();
	out.close();
	return 0;
}