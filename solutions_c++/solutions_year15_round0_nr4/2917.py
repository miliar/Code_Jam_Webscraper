#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int tc = 1;
	while(tc <= t)
	{
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		int ans = 0; // 0 -> Gabriel(grid is filled), 1->(Richard)
		if(x == 1)
			ans = 0;
		else if(x == 2)
		{
			if(r%2 == 1 && c%2 == 1)
				ans = 1;
			else
				ans = 0;
		}
		else if(x == 3)
		{
			if(r == 1 || c == 1)
				ans = 1;
			else if(r == 3 || c == 3)
				ans = 0;
			else
				ans = 1;
		}
		else if(x == 4)
		{
			if((r == 4 && c >= 3) || (r >= 3 && c == 4))
				ans = 0;
			else
				ans = 1;
		}
		if(ans == 0)
			printf("Case #%d: GABRIEL\n",tc);
		else
			printf("Case #%d: RICHARD\n",tc);
		tc++;
	}
	return 0;
}
