#include<stdio.h>
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("outputfff1.in","w",stdout);
	int R,C,W,T,tcount=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d %d",&R,&C,&W);
		if(C%W==0)
		{
			printf("Case #%d: %d\n",++tcount,C/W+W-1);
		}
		else
		{
			if(C<2*W) printf("Case #%d: %d\n",++tcount,W+1);
			else     printf("Case #%d: %d\n",++tcount,C/W+W);
		}
	}
	return 0;
}
