#include<stdio.h>
char str[1001];
int main()
{
	freopen("p12.in","r",stdin);
	freopen("output.txt","w",stdout);
	int temp,sm,need,t,c,j=1;
	scanf("%d",&temp);
	while(temp--)
	{
		need=0;
		c=0;
		scanf("%d",&sm);
		scanf("%s",str);
		for(int i=0;i<=sm;i++)
		{
			t=str[i]-'0';
			if(i==0)
			{
				if(t==0)
				{
				need=1;
				c=1;
				}
				else
				c+=t;
				
			}
			else
			{
				if(c>=i)
				c+=t;
				else{
				need+=(i-c);
				c+=(i-c)+t;
				//printf("needed  %d %d %d\n",i,need,c);
			}
			}	
		}
		printf("Case #%d: %d\n",j,need);
		j++;
	}
	
}
