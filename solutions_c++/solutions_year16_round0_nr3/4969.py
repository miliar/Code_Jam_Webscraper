#include <iostream>
#include <cstdio>
using namespace std;

const int N = 33;

int n,J,T,bit[N];
long long w[11];

int prime(long long x)
{
	int i;
	if(x == 2) return 1;
	for(i = 3; 1LL * i * i <= x; ++ i)
		if(x%i == 0)
			return i;
	return 1;
}

long long pow(int a,int b)
{
	long long ans = 1;
	while(b)
	{
		if(b&1) ans = ans*a;
		a*= a;  b >>= 1;
	}
	return ans;
}

void dfs(int p)
{
	if(!J) return;
	if(p == n)
	{
		int i,j;
		long long ww;
		for(i = 2; i <= 10; ++ i)
		{
			for(ww = 0LL,j = n; j >= 1; -- j)
				ww = ww + pow(i,n-j)*bit[j];
			w[i] = prime(ww);
			if(w[i] == 1) break;
		}
		if(i == 11)
		{
			for(i = 1; i <= n; ++ i) printf("%d",bit[i]);
			for(i = 2; i <= 10; ++ i) printf(" %d",w[i]);
			puts("");
			-- J;
		}
		return;
	}
	bit[p] = 1;
	dfs(p+1);
	bit[p] = 0;
	dfs(p+1);
}

int main()
{
	//freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1; t <= T; ++ t)
	{
		scanf("%d%d",&n,&J);
		printf("Case #%d:\n",t);
		bit[1] = bit[n] = 1;
		dfs(2);
	}
	return 0;
}

