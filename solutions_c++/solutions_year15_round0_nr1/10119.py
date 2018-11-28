#include<stdio.h>
int main()
{
	int n,k=0,j,i,t,m,l;
	char a[100],s[100]={'\0'};
	scanf("%d",&t);
	for(m=0;m<t;m++)
	{
		scanf("%d",&n);
		gets(a);
		j=0;k=0;i=1;
		while(a[i]!='\0')
		{
			s[j++]=a[i++];
		}
		s[j++]='\0';
		j=0;
		for(i=0;i<=n;i++)
		{
			l=(int)s[i]-48;
			if(l==0)
			continue;
			if(i<=k)
			{
				k=k+l;
			}
			else
			{
				while(i!=k)
				{
					k=k+1;
					j++;
				}
				k=k+l;
			}
		}
		printf("Case #%d: %d\n",(m+1),j);
	}
	return 0;
}
