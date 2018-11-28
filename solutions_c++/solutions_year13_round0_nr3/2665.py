#include<stdio.h>
int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int step;
	int a,b;
	int numa,numb;
	scanf("%d",&t);
	for(step=1;step<=t;step++)
	{
		printf("Case #%d: ",step);
		scanf("%d%d",&a,&b);
		if(a<=1)numa=0;
		else if(a<=4)numa=1;
		else if(a<=9)numa=2;
		else if(a<=121)numa=3;
		else if(a<=484)numa=4;
		else numa=5;
		if(b<1)numb=0;
		else if(b<4)numb=1;
		else if(b<9)numb=2;
		else if(b<121)numb=3;
		else if(b<484)numb=4;
		else numb=5;
		printf("%d\n",numb-numa);
	}
	return(0);
}