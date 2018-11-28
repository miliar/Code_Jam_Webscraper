#include <bits/stdc++.h>
using namespace std;

int main () {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		int res = 0;
		while(s.find('-') != string::npos) {
			int i = 0;
			if(s[i] == '+')
				res++;
			while(s[i] == '+') {
				s[i] = '-';
				i++;
			}
			for(i = s.length()-1; i >= 0 && s[i] == '+'; i--);
			for(int j = 0; j <= i; j++, i--) {
				char tmp = ((s[j] == '+')?'-':'+');
				s[j] = ((s[i] == '+')?'-':'+');
				s[i] = tmp;
			}
			res++;
		}
		cout << res << endl;
	}
	return 0;
}
