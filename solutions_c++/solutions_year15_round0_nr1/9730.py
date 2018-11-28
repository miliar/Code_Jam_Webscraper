#include <stdio.h>
int main()
{
	long int i,s,n,j,p,c=0,b[2000];
	char st[2000];
	scanf("%ld",&n);
	for(i=0;i<n;i++)
	{
		scanf("%ld",&s);
		scanf("%s",st);
		p=(long int)(st[0]-48);
		c=0;
		for(j=0;j<s;j++)
		{
			if(p==0 && j==0)
			{c=1;p=1;}
			if(p>=j+1)
			{
				p=p+((long int)(st[j+1]-48));
				continue;
			}
			else
			{
			c=c+j+1-p;
			p=j+1+((long int)(st[j+1]-48));
		}
		}
		b[i]=c;
	}
	for(i=0;i<n;i++)
	printf("Case #%ld: %ld\n",i+1,b[i]);
	return 0;
}
