#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
	int t;
	cin >> t;
	string s, res;
	for(int l = 1; l <= t; l++) {
		cin >> s;
		string res;
		res = res + s[0];
		for(int i = 1; i < s.size(); i++) {
			if(s[i] >= res[0])
				res = s[i] + res;
			else
				res = res + s[i];
		}
		cout << "Case #" << l << ": " << res << endl;
	}
	return 0;
}