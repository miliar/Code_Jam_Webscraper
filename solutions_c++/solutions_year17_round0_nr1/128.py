#include<stdio.h>
int n, m;
char a[100009];
int res;
__inline char flip(char x) { return (x == '+') ? '-' : '+'; }
int main()
{
//	freopen("A-small-attempt0.in", "rt", stdin);
//	freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	int t, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%s %d", a, &m);
		for (n = 0; a[n]; n++);
		res = 0;
		for (i = 0; i+m <= n; i++)
		{
			if (a[i]=='-') {
				for (j = 0; j < m; j++) {
					a[i+j] = flip(a[i+j]);
				}
				res++;
			}
		}
		for (j = 0; j < m; j++) {
			if (a[i + j] == '-')
				res = -1;
		}
		printf("Case #%d: ", ++tv);
		if (res < 0)printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
}