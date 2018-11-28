#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
using namespace std;


char s[10005];

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for (int T = 0; T < TT; T++) {
		printf("Case #%d: ", T+1);
		int n;
		scanf("%d", &n);
		n++;
		scanf("%s", s);
		int res = 0;
		int tot = 0;
		for (int i = 0; i < n; i++) {
			if (tot < i) {
				res += i - tot;
				tot = i;
			}
			tot += s[i] - '0';
		}
		printf("%d\n", res);
	}
	return 0;
}