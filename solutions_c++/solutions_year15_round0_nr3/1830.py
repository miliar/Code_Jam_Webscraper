#include <stdio.h>

int n;
long long m;
char ch[100000];
int a[100000];

int table[4][4]={1, 2, 3, 4, 2, -1, 4, -3, 3, -4, -1, 2, 4, 3, -2, -1};

int abs(int x)
{
	return x>0?x:-x;
}

int product(int x, int y)
{
	int dab=table[abs(x)-1][abs(y)-1];
	if(x*y < 0) dab*=-1;
	return dab;
}

long long min(long long x, long long y)
{
	return x>y?y:x;
}

int main()
{
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TT);
	for(T=0;T<TT;T++)
	{
		int i, j, k;
		scanf("%d%I64d", &n, &m);
		scanf("%s", ch);
		printf("Case #%d: ", T+1);
		for(i=0;i<n;i++)
		{
			a[i]=ch[i]-'i'+2;
		}
		for(i=1;i<min(m, 8);i++)
		{
			for(j=0;j<n;j++)
			{
				a[i*n+j]=a[j];
			}
		}
		int now=1;
		int xx=-1, yy=-1;
		for(i=0;i<n;i++)
		{
			now=product(now, a[i]);
		}
		if(!(now == -1 && m%2 == 1 || now != 1 && now != -1 && m%4 == 2))
		{
			printf("NO\n");
			continue;
		}
		now=1;
		for(i=0;i<min(n*m, n*8);i++)
		{
			now=product(now, a[i]);
			if(now == 2)
			{
				xx=i;
			}
			if(xx != -1 && now == 4)
			{
				yy=i;
				break;
			}
		}
		if(yy != -1)
		{
			printf("YES\n");
		}
		else printf("NO\n");
	}
}