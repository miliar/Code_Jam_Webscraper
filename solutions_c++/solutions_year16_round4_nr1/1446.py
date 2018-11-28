#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <sstream>

using namespace std;

string gen(char c, int level) {
	if(level == 1) {
		return string(1,c);
	}
	string a,b;
	if(c == 'P') {
		a = gen('P', level-1);
		b = gen('R', level-1);
	} else if(c == 'R') {
		a = gen('R', level-1);
		b = gen('S', level-1);
	} else if(c == 'S') {
		a = gen('P', level-1);
		b = gen('S', level-1);
	}
	if(b < a) swap(a,b);
	stringstream ss;
	ss << a << b;
	return ss.str();
}

int count(string s, char c) {
	int k(s.length());
	int sum(0);
	for(int i = 0;i < k; ++i) {
		sum += (s[i] == c);
	}
	return sum;
}

bool works(char c, int n, int p, int r, int s) {
	string t = gen(c,n);
	bool yes = count(t,'P') == p && count(t,'R') == r && count(t,'S') == s;
	return yes;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		int n,p,r,s;
		cin >> n >> r >> p >> s;
		n = n+1;
			// cout << gen('P',n) << endl;
			// cout << gen('R',n) << endl;
			// cout << gen('S',n) << endl;
		cout << "Case #" << t << ": ";
		if(works('P',n,p,r,s)) {
			cout << gen('P',n) << endl;
		} else if(works('R',n,p,r,s)) {
			cout << gen('R',n) << endl;
		} else if(works('S',n,p,r,s)) {
			cout << gen('S',n) << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}