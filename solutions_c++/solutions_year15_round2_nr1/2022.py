#include <bits/stdc++.h>
#define LIMIT 1000000
using namespace std;

int ans[LIMIT+1] = {0};
int pd[LIMIT+1] = {0};

int rev(int x)
{
	int ret = 0;
	while(x)
	{
		ret*=10;
		ret+= x%10;
		x/=10;
	}
	return ret;
}

int solve(int x)
{
	if (x == 0)
		return 0;
		
	if (pd[x] != 0)
		return pd[x];
	
	int r = rev(x);
	
	if (r < x && x%10)
		pd[x] = min(solve(r)+1, solve(x-1)+1);
	else
		pd[x] = solve(x-1)+1;
		
	return pd[x];
}

int main()
{
	int i, j;
	int T, x, count = 1;
	
	for (i = 100000; i<=LIMIT; i+=100000) //avoid stack overflows
		solve(i);
	
	
	scanf("%d", &T);
	while(count <= T)
	{
		scanf("%d", &x);
		printf("Case #%d: %d\n", count++, solve(x));
	
	}
	return 0;
}
