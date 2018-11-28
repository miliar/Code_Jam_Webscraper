#include <iostream>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

int T, l, shy_max;
char s[1005];

bool cando(int x) {
	int curr = x;
	REP(i,l) {
		//cout << x << " " << (curr) << " " << (s[i]-'0') << endl;
		if (curr >= i) {
			curr += s[i]-'0';
		} else {
			return false;
		}
	}
	return true;
}

int main() {
	cin >> T;
	REP(qqq,T) {
		cin >> shy_max;

		cin >> s;
		l = strlen(s);

		int x = 0;
		while (!cando(x)) x++;
		cout << "Case #" << (qqq+1) << ": " << x << endl;
	}
}
