#include <stdio.h>

using namespace std;

int main()
{
	int x,r,c,q,k,min,mid;
	// freopen("test.in","r",stdin);
	// freopen("test.out","w",stdout);
	scanf("%d",&q);
	for(k=1;k<=q;k++)
	{
		printf("Case #%d: ",k);
		scanf("%d %d %d",&x,&r,&c);
		min=r;
		mid=x/2;
		if(x%2) mid++;
		if(min > c) min=c;
		if(x==1)
			printf("GABRIEL\n");
		else if(x==2&&(r*c)%x==0)
			printf("GABRIEL\n");
		else if(x>=7)
			printf("RICHARD\n");
		else if((r*c)%x)
			printf("RICHARD\n");
		else if(r<x&&c<x)
			printf("RICHARD\n");
		else if(min<mid)
			printf("RICHARD\n");
		else if(x>=4&&min==mid)
			printf("RICHARD\n");
		else
			printf("GABRIEL\n");
	}
	return 0;
}