#include <iostream>
#include <stdio.h>
#include <map>
#include <algorithm>

using namespace std;

map<string, char> mp;

void doit(int &sgn, char &c, char si) {
	string tmp = string("") + c + si;
		if (c == '1') {
			c = si;
		} else if (si == '1') {
			
		} else if (si == c) {
			sgn = -sgn;
			c = '1';
		} else if (mp.find(tmp) != mp.end()) {
			c = mp[tmp];
		} else {
			reverse(tmp.begin(), tmp.end());
			sgn = -sgn;
			c = mp[tmp];
		}
}

typedef long long LL;



bool cando(int n, LL x, string s, string ans) {
	int l1, l2, l3;
	int sgn1 = 1, sgn2 = 1, sgn3 = 1;
	char c1 = '1', c2 = c1, c3 = c1;
	bool suc = true;
	for (l1 = 0; l1 < n * (LL)x; l1 ++) {
			doit(sgn1, c1, s[l1 % n]);
		///	cout << sgn1 << ' ' << c1 << endl;
			if (sgn1 == 1 && c1 == ans[0]) {
				break;
			}
			if (l1 > n * 200) {
				suc = false;
				break;
			}
	}		
	for (l2 = l1 + 1; l2 < n * (LL)x; l2 ++) {
			doit(sgn2, c2, s[l2 % n]);
			if (sgn2 == 1 && c2 == ans[1]) {
				break;
			}
			if (l2 > n * 200) {
				suc = false;
				break;
			}
	}
	for (l3 = l2 + 1; l3 < n * (LL)x; l3 ++) {
			if (l3 % n == 0) {
				break;
			}
			doit(sgn3, c3, s[l3 % n]);
			//cout << sgn3 << ' ' << c3 << endl;
	}
	//	printf("l1 = %d, l2 = %d, l3 = %d\n", l1, l2, l3);
	
	if (l3 > n * (LL) x) {
			suc = false;
	}
	x -= l3 / n;
	//	printf("x = %d\n", x);
	if (x) {
				int sss = 1;
				char ccc = '1';
				for (int i = 0; i < n; i ++) {
					doit(sss, ccc, s[i]);
				}
			//	printf("ccc = %c\n", ccc);
			//	printf("sss = %d, ccc = %c\n", sss, ccc);
			//	printf("sgn3 = %d, c3 = %c\n", sgn3, c3);
				if (x > 4) x %= 4;
				if (x % 2 && sss == -1) sss = -1;
				else sss = 1;
				char c = ccc;
				ccc = '1';
		//		printf("ccc = %c, c = %c\n", ccc, c); 
				for (int i = 0; i < x; i ++) {
					doit(sss, ccc, c);
				}
				if (sss == -1) sgn3 = -sgn3;
	//			printf("ccc = %c\n", ccc);
				doit(sgn3, c3, ccc);
	}
		//	printf("sgn3 = %d, c3 = %c\n", sgn3, c3); 
	if (sgn3 != 1 || c3 != ans[2]) {
		suc = false;
	}
	return suc;
}

int main() {
	freopen("C:/Users/dd/Downloads/C-large (1).in", "r", stdin);
	freopen("C:/Users/dd/Downloads/C-large.out", "w", stdout);
	mp["ij"] = 'k';
	mp["jk"] = 'i';
	mp["ki"] = 'j';
	int cas;
	cin >> cas;
	for (int te = 1; te <= cas; te ++) {
		int n;
		LL x;
		cin >> n >> x;
		string s, ans = "ijk";
		cin >> s;
		bool suc = cando(n, x, s, "ijk");
		
		printf("Case #%d: %s\n", te, suc ? "YES" : "NO");
	}
}
