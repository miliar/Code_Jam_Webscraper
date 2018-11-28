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

char s[100005];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		int n;
		scanf("%d", &n);
		scanf("%s", s);
		int ans = 0, sum = 0;
		for (int i = 0; i <= n; i++) {
			ans = max(ans, max(0, i - sum)), sum += s[i] - '0';
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	
	return 0;
}