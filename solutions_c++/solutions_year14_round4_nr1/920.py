#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;


int a[10005];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);


	int TT;
	scanf("%d", &TT);
	for(int T = 0; T < TT; T++)
	{
		printf("Case #%d: ", T+1);
		int n, x;
		scanf("%d%d", &n, &x);
		for(int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a+n);

		int l = 0, r = n-1, res = 0;
		while(r >= l)
		{
			if(a[l] + a[r] <= x)
			{
				res++;
				l++;
				r--;
			}
			else
			{
				res ++;
				r--;
			}
		}
		printf("%d\n", res);
	}

	return 0;
}