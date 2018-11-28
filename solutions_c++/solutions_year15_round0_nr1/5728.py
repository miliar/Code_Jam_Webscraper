//gcj A

#include <iostream>
#include <string.h>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
using namespace std;

#define LL __int64
#define MOD 1000000007

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, i, n, c, r, ca = 1;
	char s[1005];
	scanf("%d", &T);
	while (T--){
		scanf("%d", &n);
		scanf("%s", s);
		c = s[0] - '0';
		r = 0;
		for (i = 1; i <= n; i++){
			if (c < i){
				r += i - c;
				c = i + s[i] - '0';
			}
			else {
				c += s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", ca++, r);
	}
	return 0;
}