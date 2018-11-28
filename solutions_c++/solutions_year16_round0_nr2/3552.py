#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T;
char c, s[1000];

int main() {
	int t = 1, i, res;
	scanf("%d", &T);
	while (T--) {
		scanf(" %s ", s);
		res = 0;
		c = '+';
		for (i=strlen(s)-1; i>=0; i--) {
			if (s[i] != c) {
				c = (c == '+' ? '-' : '+');
				res++;
			}
		}
		printf("Case #%d: %d\n", t++, res);
	}
	return 0;
}