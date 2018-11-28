#include<stdio.h>
main()
{
	freopen("read2.in","r",stdin);
	freopen("write2.out","w",stdout);
	int t,cs,i,j,k,len,count;
	scanf("%d",&t);
	char a[1001];
	for(cs=1;cs<=t;cs++)
	{
		scanf("%s",&a);
		i=0;
		scanf("%d",&k);
		while(a[i]!='\0')
			i++;
		len=i;
		i=0;
		count=0;
		while(i<=len-k)
		{
			if(a[i]=='-')
			{
				count++;
				j=i;
				for(j=i;j<i+k;j++)
				{
					if(a[j]=='-')
						a[j]='+';
					else if(a[j]=='+')
						a[j]='-';
				}
			}
			i++;
		}
		for(i;i<len;i++)
		{
			if(a[i]=='-')
				break;
		}
		printf("Case #%d: ",cs);
		if(i==len)
			printf("%d\n",count);
		else
			printf("IMPOSSIBLE\n");
	}
}
