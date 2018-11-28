#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

string s;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int loop = 1; loop <= T; loop++) {
		cout << "Case #" << loop << ": ";
		cin >> s;
		int N = s.size();
		int c = 0;
		for(int i = N - 1; i >= 0; i--) {
			if(s[i] == '+' && c % 2 == 1) {
				c++;
			}
			else if(s[i] == '-' && c % 2 == 0) {
				c++;
			}
		}

		cout << c << endl;
	}

}