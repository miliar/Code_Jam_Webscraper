#include <bits/stdc++.h>
using namespace std;

int z, n, cur, res;
char s[1001];

int main() {
	scanf("%d", &z);
	for(int c = 1; c <= z; c++) {
		cur = res = 0;
		scanf("%d%s", &n, s);
		for(int i = 0; i <= n; i++) {
			if(i>0) {
				res+=max(0, i-cur);
				cur+=max(0, i-cur);
			}
			cur+=(s[i]-'0');
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
