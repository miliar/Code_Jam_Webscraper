#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(int k, int c, int s)
{
	if(s==k)
	{
		for(int i=1;i<=s;i++)
			printf(" %d", i);
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	int k,c,s;
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", tc);
		solve(k, c, s);
		printf("\n");
	}
	return 0;
}