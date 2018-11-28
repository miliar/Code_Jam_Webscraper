#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("output_3.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tst =1;tst <= t;tst++)
	{
		int x,r,c;

		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",tst);
		if(x == 1)
		{
			puts("GABRIEL");
		}else if(x == 2)
		{
			if((r*c) & 1 ) puts("RICHARD");
			else puts("GABRIEL");
		}else if(x == 3)
		{
			if((r == 3 || c == 3) && ((r*c) != 3))puts("GABRIEL");
			else puts("RICHARD");
		}else{
			if((r == 3 && c == 4) || (r == 4 && c ==3) || (r == 4 && c == 4)) puts("GABRIEL");
			else puts("RICHARD");
		}
	}
}
