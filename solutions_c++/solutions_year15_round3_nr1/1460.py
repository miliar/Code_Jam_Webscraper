#include<iostream>
#include <stdio.h>
using namespace std;
int  R, C, W, T;
int ans;
int input()
{
		scanf("%d %d %d",&R,&C,&W);
		return 0;
}

int deal()
{
		if(R==1)
		{
			if(C%W==0) ans = C/W-1;
			else ans = C/W;
		}
		else
		{
			if(C%W==0) ans = C*R/W-1;
			else ans = R*(C/W);
		}

		ans+=W;
		printf("%d\n",ans);
		return 0;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d",&T);
	for(int cases=0;cases<T;++cases)
	{
		printf("Case #%d: ", cases+1);
		input();
		deal();
	}
	return 0;
}

