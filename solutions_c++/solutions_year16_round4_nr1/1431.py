#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include "stdio.h"

using namespace std;

string sortit(string s, int n) {
	int tp = n;
	int len = 1;
	while (tp--) {
		int pt = 0;
		while(pt < s.length()) {
			if (s.substr(pt, len) > s.substr(pt+len, len)) {
				string ns = s.substr(0, pt) + s.substr(pt+len, len) + s.substr(pt, len) + s.substr(pt+2*len);
				s = ns;
			}
			pt += 2*len;
		}
		len *= 2;
	}
	return s;
}

int main() {
	int t;
	cin >> t;

	string tems[15];
	int acs[15], bcs[15], ccs[15];
	tems[2] = "acbc";
	acs[2] = 1;
	bcs[2] = 1;
	ccs[2] = 2;
	for (int i = 3; i <= 12; ++i) {
		tems[i] = "";
		for (int j = 0; j < tems[i-1].length(); ++j) {
			if (tems[i-1][j] == 'a')
				tems[i] += "ab";
			else if (tems[i-1][j] == 'b')
				tems[i] += "bc";
			else
				tems[i] += "ca";
		}
		acs[i] = acs[i-1] + ccs[i-1];
		bcs[i] = bcs[i-1] + acs[i-1];
		ccs[i] = ccs[i-1] + bcs[i-1];
	}

	int n;
	int r,p,s;
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> n >> r >> p >> s;

		cout << "Case #" << tcount << ": ";

		if (n == 1) {
			if (r == 1 && p == 1 && s == 0) {
				cout << "PR\n";
				continue;
			}
			if (r == 1 && p == 0 && s == 1) {
				cout << "RS\n";
				continue;
			}
			if (r == 0 && p == 1 && s == 1) {
				cout << "PS\n";
				continue;
			}
			cout << "IMPOSSIBLE\n";
			continue;
		}
		if (n == 2) {
			string tem = "acbc";
			char a, b, c;
			if (p == 1 && r == 1 && s == 2) {
				a = 'P';
				b = 'R';
				c = 'S';
			}
			else if (p == 2 && r == 1 && s == 1) {
				a = 'R';
				b = 'S';
				c = 'P';
			}
			else if (p == 1 && r == 2 && s == 1) {
				a = 'S';
				b = 'P';
				c = 'R';
			}
			else {
				cout << "IMPOSSIBLE\n";
				continue;
			}
			for (int i = 0; i < tem.length(); ++i) {
				if (tem[i] == 'a')
					tem[i] = a;
				else if (tem[i] == 'b')
					tem[i] = b;
				else
					tem[i] = c;
			}
			cout << sortit(tem, n) << endl;
			continue;
		}

		string tem = tems[n];
		char a, b, c;
		if (p == acs[n] && r == bcs[n] && s == ccs[n]) {
			a = 'P';
			b = 'R';
			c = 'S';
		}
		else if (p == ccs[n] && r == acs[n] && s == bcs[n]) {
			a = 'R';
			b = 'S';
			c = 'P';
		}
		else if (p == bcs[n] && r == ccs[n] && s == acs[n]) {
			a = 'S';
			b = 'P';
			c = 'R';
		}
		else {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		for (int i = 0; i < tem.length(); ++i) {
			if (tem[i] == 'a')
				tem[i] = a;
			else if (tem[i] == 'b')
				tem[i] = b;
			else
				tem[i] = c;
		}
		cout << sortit(tem, n) << endl;
		continue;

		//if (n == 3) {
		//	string tem = "abcabcca";
		//	char a, b, c;
		//	if (p == 3 && r == 2 && s == 3) {
		//		a = 'P';
		//		b = 'R';
		//		c = 'S';
		//	}
		//	else if (p == 3 && r == 3 && s == 2) {
		//		a = 'R';
		//		b = 'S';
		//		c = 'P';
		//	}
		//	else if (p == 2 && r == 3 && s == 3) {
		//		a = 'S';
		//		b = 'P';
		//		c = 'R';
		//	}
		//	else {
		//		cout << "IMPOSSIBLE\n";
		//		continue;
		//	}
		//	for (int i = 0; i < tem.length(); ++i) {
		//		if (tem[i] == 'a')
		//			tem[i] = a;
		//		else if (tem[i] == 'b')
		//			tem[i] = b;
		//		else
		//			tem[i] = c;
		//	}
		//	cout << sortit(tem, n) << endl;
		//	continue;
		//}

		

		cout << "IMPOSSIBLE\n";
	}

	return 0;
}