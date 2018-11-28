#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;
int T, x, y;
string dir = "NESW";
int D[4] = {1, -1, 1, -1};

string direction(int x, int y) {
	string res = "";
	if (x > 0) res += "E";
	else res += "W";
	if (y > 0) res += "N";
	else res += "S";
	return res;

}
char op(char c) {
	if (c == 'N') return 'S';
	if (c == 'S') return 'N';
	if (c == 'E') return 'W';
	if (c == 'W') return 'E';
	return 0;
}

void solve(int t) {
	scanf("%d%d", &x, &y);
	string s = direction(x, y);
	string ans = "";
	x = abs(x);
	y = abs(y);
	for (int i = 1 ; i <= x ;i ++) {
		ans += op(s[0]);
		ans += s[0];
	}
	for (int i = 1 ; i <= y ;i ++) {
		ans += op(s[1]);
		ans += s[1];
	}
	printf("Case #%d: ", t);
	cout << ans << endl;



}


int main() {
	scanf("%d", &T);
	for (int i = 1 ; i <= T; i ++) solve(i);
	
	
	return 0;
}