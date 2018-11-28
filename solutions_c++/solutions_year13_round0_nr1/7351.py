#include <stdio.h>

int n=4;
char M[5][5];

int min(int a,int b){if(a<b)return a;return b;}

bool cmp(char a, char b) {
	return (a == b || a == 'T');
}
bool ch(char c)
{
	int i,j;
	int ret;
	for (i=1; i<=n; i++) {
		ret=1;
		for (j=1; j<=n; j++)
			ret=min(ret,cmp(M[i][j],c));
		if (ret==1) break;

		ret=1;
		for (j=1; j<=n; j++) {
			ret=min(ret,cmp(M[j][i],c));
		}
		if (ret==1) break;
	}
	if (ret==1) return ret;
	ret=1;
	for (i=1; i<=n; i++)
		ret=min(ret,cmp(M[i][i],c));
	if (ret==1) return ret;
	ret=1;
	for (i=1; i<=n; i++)
		ret=min(ret,cmp(M[n-i+1][i],c));
	return ret;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,k=0;
	scanf("%d",&t);

	while (++k<=t)
	{
		int i,j;
		for (i=1; i<=n; i++)
			scanf("%s",M[i]+1);
		printf("Case #%d: ",k);
		if (ch('O')) {printf("O won\n"); continue;}
		if (ch('X')) {printf("X won\n"); continue;}

		for (i=1; i<=n; i++) {
			for (j=1; j<=n; j++)
				if (M[i][j] == '.') break;
			if (M[i][j] == '.') break;
		}
		if (M[i][j] == '.') {printf("Game has not completed\n"); continue;}
		printf("Draw\n");

	}
}
