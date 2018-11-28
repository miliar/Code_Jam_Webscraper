#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("my.out", "w", stdout);
	int a, b, k;
	int t, i, j, l = 1, c;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d", &a, &b, &k);
		c = 0;
		for (i = 0; i < a; i++) {
			for (j = 0; j < b; j++) {
				if ((i & j) < k)
					c++;	
			}
		}
		printf("Case #%d: %d\n", l++, c);
	}
	return 0;
}
