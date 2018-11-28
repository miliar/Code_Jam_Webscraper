#include <bits/stdc++.h>
using namespace std;

int main() {
	int _;
	cin >> _;
	for(int __ = 0; __ < _;) {
		cout << "Case #" << ++__ << ": ";
		string s;
		cin >> s;
		string t = s.substr(0,1);
		for(int i = 1; i < (int)s.size(); i++) {
			if(t[0] <= s[i]) t = s.substr(i, 1) + t; 
			else t += s[i];
		}
		cout << t << "\n";
	
	}	
	return 0;
}
