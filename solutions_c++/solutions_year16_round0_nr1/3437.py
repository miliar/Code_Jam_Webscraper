#include<stdio.h>
int main()
{
	int t,b,a[10],c,k;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		for(int j=0;j<10;j++)
		a[j]=0;
		scanf("%d",&b);
		k=1;
		if(b==0)
		{printf("Case #%d: INSOMNIA\n",i+1);}
		else{
		while(1)
		{
			c=k*b;
			while(c!=0)
			{
				a[c%10]=1;
				c=c/10;
			}
			k++;
			if(a[0]==1&&a[1]==1&&a[2]==1&&a[3]==1&&a[4]==1&&a[5]==1&&a[6]==1&&a[7]==1&&a[8]==1&&a[9]==1)
			break;
		}
		printf("Case #%d: %d\n",i+1,b*(k-1));}	
	}
	return 0;
}
