#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T; cin >> T;
	for(int t = 1; t <= T; t++) {
		int n; cin >> n;
		string s; cin >> s;
		int a = 0, b = 0;
		for(int i = 0; i <= n; i++) {
			s[i] -= '0';
			if (s[i] == 0) continue;
			if (a < i) a = i;
			a += s[i]; b += s[i];
		}
		cout << "Case #" << t << ": " << a - b << endl;
	}
	return 0;
}