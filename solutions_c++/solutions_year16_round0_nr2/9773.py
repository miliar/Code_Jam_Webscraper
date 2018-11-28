#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int n, cnt;
char s[200];

int solve() {
	int len = strlen(s);
	int ans = 0;

	for (int i = len - 1; i > 0; --i) {
		if (s[i] != s[i - 1]) ++ans;
	}
	if (s[len - 1] == '-') ++ans;
	return ans;
}

int main() {
	int T;
	cin>>T;
	for (int test = 1; test <= T; ++test) {
		scanf("%s", s);
		printf("Case #%d: %d\n", test, solve());  
	}
	return 0;
}