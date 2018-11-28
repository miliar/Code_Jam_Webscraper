#include<stdio.h>
int main()
{
	int k,test,t,atas,bawah,c;
	scanf("%i",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%i/%i",&atas,&bawah);
		k=2;
		c=0;
		while(k<bawah)
		{
			k=k*2;
		}
		if(k!=bawah)
		printf("Case #%i: impossible\n",t);
		else
		{
		while(atas<bawah)
		{
			atas=atas*2;
			c++;
		}
		printf("Case #%i: %i\n",t,c);
		}
	}
}
