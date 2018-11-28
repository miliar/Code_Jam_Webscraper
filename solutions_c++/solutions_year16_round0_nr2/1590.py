#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

int solve(char *s) {
	int len = strlen(s);
	int c = s[0];
	int flip = 0;
	for (int i = 1; i < len; i++) {
		if (c != s[i]) {
			flip++;
			c = s[i];
		}
	}
	if (c == '-')
		flip++;
	return flip;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		char s[1000];
		scanf("%s", s);
		int ans = solve(s);
		printf("Case #%d: %d\n", i+1, ans);
	}
}
