#include"stdafx.h"

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod2 1000000007
bool mark[15];

bool marknum(ll n)
{
	while (n)
	{
		mark[n % 10] = true;
		n /= 10;
	}
	for (int i = 0; i < 10; i++)
		if (!mark[i])
			return false;
	return true;
}



int main()
{
	int t, i, j;ll n;
	freopen("a.in", "r", stdin);
	freopen("out.txt", "w", stdout);


	scanf("%d", &t);
	bool found;
	j = 0;
	while (t--)
	{
		j++;
		memset(mark, 0, sizeof(mark));
		scanf("%lld", &n);
		found = false;
		for (i = 0; i < 10000; i++)
		{
			if (marknum(i*n))
			{
				found = true;
				break;
			}
		}
			printf("Case #%d: ", j);
			if (found)
				printf("%lld\n", i*n);
			else
				printf("INSOMNIA\n");


	}

	return 0;
}