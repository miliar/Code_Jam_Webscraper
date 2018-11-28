#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	string s;
	cin >> T;
	for(int qq=1;qq<=T;qq++) {
		printf("Case #%d: ",qq);
		cin >> s;
		int i=0,moves=0;
		//store the initial char
		char c = s[0];
		

		while(i<s.length()) {
			while(s[i] == c && i<s.length()) {
				i++;
			}
			if(i< s.length() && s[i] != c)  moves++; 
			if(i < s.length() ) (c=='+')?c='-':c='+'; // flip on moves
			i++;
		}

		if(c=='-') moves++; // if last one is '-' the moves++
		

		// all neg or pos checking !!
		bool all_p = true;
		bool all_n = true;
		
		for(int i=0;i<s.length();i++) {
			if(s[i] != '+') all_p = false;
			if(s[i] != '-') all_n = false;
		}
		//------------------

		if(all_p) cout << 0 << endl;
		else if(all_n) cout << 1 << endl;
		else {
			cout << moves << endl;
		}

	}
	return 0;
}