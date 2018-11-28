#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
using namespace std;

typedef long long ll;
#define REP(i,n) for(int i = 0; i < n; i++)

void makepos(char& a, bool& flag) {
	if (a == 'I') a = 'i', flag ^= true;
	else if (a == 'J') a = 'j', flag ^= true;
	else if (a == 'K') a = 'k', flag ^= true;
	else if (a == '-') a = '1', flag ^= true;
}
void makecorr(char& a, bool& flag) {
	if (flag) {
//		cout << "!" << endl;
		if (a == 'i') a = 'I', flag ^= true;
//		cout << a << endl;
		else if (a == 'j') a = 'J', flag ^= true;
		else if (a == 'k') a = 'K', flag ^= true;
		else if (a == '1') a = '-', flag ^= true;
		else if (a == '-') a = '1', flag ^= true;
		else if (a == 'I') a = 'i', flag ^= true;
		else if (a == 'J') a = 'j', flag ^= true;
		else if (a == 'K') a = 'k', flag ^= true;
		else assert(false);
	}
}

char mult(char a, char b) {
	bool flag = false;
	makepos(a, flag);
	makepos(b, flag);

	char c;
	if (a == '1') {
		c = b;
	} else if (a == 'i') {
		if (b == '1') c = 'i'; if (b == 'i') c = '-';
		if (b == 'j') c = 'k'; if (b == 'k') c = 'J';
	} else if (a == 'j') {
		if (b == '1') c = 'j'; if (b == 'i') c = 'K';
		if (b == 'j') c = '-'; if (b == 'k') c = 'i';
	} else if (a == 'k') {
		if (b == '1') c = 'k'; if (b == 'i') c = 'j';
		if (b == 'j') c = 'I'; if (b == 'k') c = '-';
	}

//	cout << c << " " << flag << endl;
	makecorr(c, flag);
//	cout << c << endl;
	return c;
}

ll t, l, x;
char s[10005], s2[10005], suffix[10005];

int main() {
//	cout << mult('i', '-') << endl;

	cin >> t;
//	cout << t << endl;

	REP(qqq,t) {
		cin >> l >> x >> s2;

		bool ok = false;

		//slow version
		ll L = l*x;
//		cout << l << " " << x << " " << L << endl;
		REP(i,x) strcpy(&s[l*i], s2);
//		cout << s << endl;

//		cout << "!" << endl;

		suffix[L] = '1';
		for (int i = L-1; i >= 0; i--) {
			suffix[i] = mult(s[i], suffix[i+1]);
		}

		char a = '1';
		REP(i,L) {
			if (a == 'i') {
				char b = '1';
				for (int j = i; j < L; j++) {
					b = mult(b, s[j]);
					if (b == 'j' && suffix[j+1] == 'k')
						ok = true;
				}
			}
			a = mult(a, s[i]);
//			cout << a << " ";
		}
//		cout << endl;

		cout << "Case #" << (qqq+1) << ": " << (ok?"YES":"NO") << endl;
	}
}
