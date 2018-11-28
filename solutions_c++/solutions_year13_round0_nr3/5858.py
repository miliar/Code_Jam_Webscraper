#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int ans[1010];

void solve(int t) {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("Case #%d: %d\n", t, ans[b] - ans[a-1]); 
}

bool ispal(int x) {
	stringstream ss;
	ss << x;
	string s = ss.str();
	string q = s;
	reverse(s.begin(), s.end());
	if (q == s) return true;
	return false;
}

bool sqandfair(int x) {
	int sq = (int)sqrt(1.0*x);
	if (sq*sq != x) return false;
	if (ispal(sq) && ispal(x)) return true;
	return false;
	
}

int main() {
	for (int i = 1 ; i <= 1010 ; i ++) {
		ans[i] = ans[i-1];	
		if (sqandfair(i)) ans[i] ++;
	}
	int T;
	scanf("%d", &T);
	for (int i = 1 ; i <= T ; i ++) solve(i);
	return 0;
}