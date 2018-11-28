#include <bits/stdc++.h>
int main(int argc, char const *argv[])
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int X,R,C;
		scanf("%d %d %d",&X,&R,&C);
		if((X-1>R)||(X-1>C))
		{
			printf("Case #%d: RICHARD\n",t);
		}
		else if(X<=(R*C))
		{
			if((R*C)%X!=0)
				printf("Case #%d: RICHARD\n",t);
			else
				printf("Case #%d: GABRIEL\n",t);
		}
	}
	return 0;
}