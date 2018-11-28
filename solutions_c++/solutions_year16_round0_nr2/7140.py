#include <bits/stdc++.h>
using namespace std;

int ca = 0;
int tt = 0;
int flag = 0;
char s[110];

int work() {
	int len = strlen(s);
	s[len] = '+';
	int ans = 0; 

	for (int i = 0; i < len; ++i) {
		if (s[i] != s[i+1]) ++ans;
	}

	printf("Case #%d: %d\n", ++ca, ans);
}

int main() {
	scanf("%d", &tt);
	for(int c = 0; c < tt; ++c) {
		scanf("%s", s);
		work();
	}
}