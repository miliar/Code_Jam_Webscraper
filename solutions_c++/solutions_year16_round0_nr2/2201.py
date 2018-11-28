#include <bits/stdc++.h>
using namespace std;

long long T;
string s;

long long digits(long long x) {
	long long ret = 0;
	while(x) {
		ret |= 1 << (x % 10);
		x /= 10;
	}
	return ret;
}

int main() {
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		cin >> s;
		int x = 0;
		for(int i=1; i<s.length(); ++i)
			if(s[i] != s[i-1]) ++x;
		if(s[s.length()-1] == '-') ++x;
		cout << "Case #" << t << ": ";
		cout << x << '\n';
	}
}


