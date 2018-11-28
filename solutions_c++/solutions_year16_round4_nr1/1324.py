#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

string find(char c, int n) {
	if (n == 1) {
		if (c == 'P') return "PR";
		if (c == 'R') return "RS";
		if (c == 'S') return "PS";
	}
	string s1, s2;
	if (c == 'P') {
		s1 = find('P', n - 1);
		s2 = find('R', n - 1);
	}
	if (c == 'S') {
		s1 = find('P', n - 1);
		s2 = find('S', n - 1);

	}
	if (c == 'R') {
		s1 =  find('S', n - 1);
	 	s2 = find('R', n - 1);
	}
	if (s1 < s2) {
		return s1 + s2;
	}
	return s2 + s1;
}

string solve() {
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	int cp = 1, cr = 0, cs = 0;
	for(int i = 0; i < n; ++i) {
		int cp2 = cp + cs;
		int cr2 = cp + cr;
		int cs2 = cr + cs;
		cp = cp2; cr = cr2, cs = cs2;
	}
	if (cp == p && cr == r && cs == s) {
		return find('P', n);	
	}
	if (cp == r && cr == s && cs == p) {
		return find('R', n);
	}
	if (cp == s && cr == p && cs == r) {
		return find('S', n);
	}
	return "IMPOSSIBLE";
}

int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
		cout << "Case #" << x << ": " << solve() << endl;//result 
	}
	return 0;
}
