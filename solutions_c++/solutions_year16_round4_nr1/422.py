#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<vector>
#include<string>
using namespace std;


// R>S>P>R

int ct[4], b[4];
string f[14][5];
string ch[] = {"R", "P", "S"};
int n;
int order[] = {1, 0, 2};

int toint(char x) {
	if (x == 'R') return 0;
	else if (x == 'P') return 1;
	return 2;
}

int cmp(string s1, string s2) {
	int len = s1.size();
	for (int i = 0; i < len; ++i) {
		if (order[toint(s1[i])] > order[toint(s2[i])]) return 1;
	}
	return -1;
}

string dp(int x, int y) {
	if (x == n) return string(ch[y]);
	if (f[x][y] != "") return f[x][y];
	string s1, s2;
	if (y == 0) {
		s1 = dp(x + 1, 2);
		s2 = dp(x + 1, 0);
	} else if (y == 1) {
		s1 = dp(x + 1, 0);
		s2 = dp(x + 1, 1);
	} else {
		s1 = dp(x + 1, 1);
		s2 = dp(x + 1, 2);
	}
	if (cmp(s1, s2) < 0) {
		f[x][y] = s1 + s2;
	} else {
		f[x][y] = s2 + s1;
	}
	return f[x][y];
}

void work() {
	scanf("%d", &n);
	memset(b, 0, sizeof(b));
	memset(ct, 0, sizeof(ct));
	for (int i = 0; i < 3; ++i) {
		scanf("%d", &b[i]);
	}
	string ans = "";
	for (int i = 0; i <	3; ++i) {
		for (int j = 0; j <= n; ++j) {
			for (int k = 0; k < 5; ++k) {
				f[j][k] = "";
			}
		}
		string s = dp(0, i);
		memset(ct, 0, sizeof(ct));
		for (int j = 0; j < (1<<n); ++j) ct[toint(s[j])]++;
		bool flag = true;
		for (int j = 0; j < 3; ++j) {
			if (ct[j] != b[j]) {
				flag = false;
				break;
			}
		}
		if (flag) {
			if (ans == "") ans = s;
			else {
				if (cmp(ans, s) > 0) ans = s;
			}
		}
	}
	if (ans == "") printf("IMPOSSIBLE\n");
	else printf("%s\n", ans.c_str());
}


int main() {
	freopen("A-large.in", "r", stdin);
	int TestCase;
	scanf("%d", &TestCase);
	for (int i = 1; i <= TestCase; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	
	return 0;
}