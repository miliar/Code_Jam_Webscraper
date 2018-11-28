#include<stdio.h>
int t,i,j,l,count=0,flag;
char s[10],st[100][10];
int main()
{
	j=0,flag=0;
	
	
	scanf("%d",&t);
	//for(i=1;i<=t;i++)
		//scanf("%s",st[i]);
	for(i=1;i<=t;i++)
	{	
		flag=0;
		scanf("%s",s);
		count=0;
		j=0;
		l=0;
		printf("Case %d: ",i);
		while(s[j]!='\0')
		{	
			flag=0;
			if(s[j]=='-')
				flag=1;
			if(flag==0 && s[j+1]=='\0')
				break;
			if(s[j]!=s[j+1])
			{
				count++;
				for(l=0;l<=j;l++)
				{
					if(flag==1)
						s[l]='+';
					else
						s[l]='-';
				}
			}
			
			j++;	
		}
		printf("%d\n",count);
	}
}						
					
					
