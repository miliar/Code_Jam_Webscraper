#include <stdio.h>

const char* solve(int n, int p, int r, int s)
{
	if(p<0 || r<0 || s<0) return NULL;
	if(n==1)
	{
		if(p==2 || r==2 || s==2) return NULL;
		if(p==0) return "RS";
		if(r==0) return "PS";
		return "PR";
	}
	int X = (p+r+s)/2, x=0;
	const char *t = solve(n-1, X-s, X-r, X-p);
	if(t == NULL) return NULL;
	char *re = new char[1+(1<<n)];
	for(int i=0; i<(1<<(n-1)); i++)
	{
		if(t[i] == 'P')
		{
			re[x++] = 'P';
			re[x++] = 'R';
		}
		if(t[i] == 'R')
		{
			re[x++] = 'P';
			re[x++] = 'S';
		}
		if(t[i] == 'S')
		{
			re[x++] = 'R';
			re[x++] = 'S';
		}
	}
	re[x] = 0;
	if(n>2) delete[] t;
	return re;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++)
	{
		int n, p, s, r;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		const char* t = solve(n, p, r, s);
		if(t==NULL) printf("Case #%d: IMPOSSIBLE\n", i);
		else
		{
			printf("Case #%d: %s\n", i, t);
			if(n>=2) delete[] t;
		}
	}
	return 0;
}