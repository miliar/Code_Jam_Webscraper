#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	getchar();
	int x=1;
	for(;x<=t;x++)
	{
		int n;
		char s[1001];
		scanf("%d",&n);
		getchar();
		scanf("%s",s);
		int i=0;
		int sum=0;
		int add=0;
		while(s[i]!='\0')
		{
			if(s[i]!='0')
			{
				if(i>sum)
				{
					add=add+i-sum;
					sum=i+(int(s[i])-48);
					//printf("%d %d\n",i,sum);
				}
				else
				{
					sum+=(int(s[i])-48);
				}
			}
		//	printf("%d %d %d\n",i,add,sum);
			i++;
		}
		printf("Case #%d: %d\n",x,add);
	}
	return 0;
}
