// Counting sheep 

#include <iostream>
#include <cstdio>

using namespace std;

#define M 10

int dg[M];

void init()
{
	for(int i = 0; i < M; ++i)dg[i] = 0;
	return;
}

int check()
{
	for(int i = 0; i < M; ++i)
	{
		if(dg[i] == 0)return 0;
	}
	return 1;
}

void mark(int x)
{
	while(x)
	{
		dg[x % 10] = 1;
		x /= 10;
	}
	return;
}

int main()
{
	int tc, cs = 1;
	cin >> tc;
	while(tc--)
	{
		int n, nc;
		cin >> n;
		nc = n;
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", cs++);
			continue;
		}
		int c = 2; int ans;
		init();
		while(1)
		{
			mark(n);
			if(check()){
			  ans = n;
			  break;
			}
			n = c * nc;
			c++;
		}
		printf("Case #%d: %d\n", cs++, ans);
	}
		return 0;	
}
