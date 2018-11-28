#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

void run() {
	string ori;
	string ans = "";
	cin >> ori;
	for (size_t i = 0; i < ori.length(); ++i) {
		string tmp1 = ans + ori[i];
		string tmp2 = ori[i] + ans;
		ans = (tmp1 > tmp2 ? tmp1 : tmp2);
	}
	cout << ans << endl;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A_output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		cout << "Case #" << cas << ": ";
		run();
	}
	return 0;
}
