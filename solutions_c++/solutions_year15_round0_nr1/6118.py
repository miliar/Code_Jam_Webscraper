#include<stdio.h>

int main()
{
	FILE *fp,*fp1;
	
	fp=freopen("A-large.in","r",stdin);
	fp1=freopen("c.text","w+",stdout);
	
	int t,smax,i,j;
	long ans,count;
	char s[2000];
	
	scanf("%d",&t);
	
	for(j=0;j<t;j++)
	{
		count=0;
		ans=0;
		scanf("%d",&smax);
		scanf("%s",s);
		
		for(i=0;i<smax+1;i++)
			if(count>=i)
				count+=s[i]-48;
			else
			{
				ans+=i-count;
				count+=i-count+s[i]-48;
			}
		printf("Case #%d: %ld\n",j+1,ans);
	}
	
	fclose(fp);
	fclose(fp1);
}
