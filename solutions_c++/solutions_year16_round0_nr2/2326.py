#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>

using namespace std;

long long t, ans;
string s;

int main() {
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	cin >> t;
	for (int i = 1; i <= t; i++) {
		ans = 0;
		cin >> s;
		for (int j = s.size() - 1; j >= 0; j--)
		if (ans % 2 == 0) {
			if (s[j] == '-')
				ans++;
		}
		else {
			if (s[j] == '+')
				ans++;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}