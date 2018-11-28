#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
int main(void) {
	int totalCase, cases;
	int i, j, k, len, ans;
	bool done;
	string s;
	ifstream cin("l.in");
	ofstream cout("l.out");
	cin >> totalCase;
	for (cases = 1; cases <= totalCase; cases++) {
		cin >> s;
		len = s.length();
		ans = 0;
		while (1) {
			done = true;
			for (i = 0; i < len; i++) {
				if (s[i] == '-')done = false;
			}
			if (done)break;
			if (s[0] == '-') {
				for (i = 0; i < len; i++) {
					if (s[i] == '+')break;
					s[i] = '+';
				}
			}//////////
			else{
				for (i = 0; i < len; i++) {
					if (s[i] == '-')break;
					s[i] = '-';
				}
			}//////////
			ans++;
		}
		cout << "Case #" << cases << ": " << ans << endl;
	}
	system("pause");
	return 0;
}
