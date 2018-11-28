#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int smax;
string s;

int main() {
	int t;
	cin >> t;

	for (int cs = 1; cs <= t; ++cs) {
		cin >> smax;
		cin >> s;
		
		int cnt = 0, sol = 0; 
		for (int i = 0; i <= smax; ++i) {
			if (s[i] != '0' && i > cnt) {
				sol += (i - cnt);
				cnt += (i - cnt);
			}
			cnt += (s[i]-'0');
		}
		cout << "Case #" << cs << ": " << sol << endl;
	}

	return 0;
}
