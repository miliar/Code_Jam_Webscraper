#include<stdio.h>

int main()
{	
	int t,m=0,len,sum,i,ans;
	char s[1005];
	
	FILE *fp=fopen("A-large.in","r");
	fscanf(fp,"%d",&t);
	FILE *fp1=fopen("Abhinavanslarge.txt","w+");
	
	while(m!=t)
	{
		sum=0;
		ans=0;
		
		fscanf(fp,"%d",&len);
		
		fscanf(fp,"%s",s);
		
		sum+=(s[0]-'0');
		
		for(i=1;i<=len;i++)
		{
			if(sum<i &&s[i]!='0')
			{
				ans+=(i-sum);
				sum=i;
			}
			
			sum+=(s[i]-'0');
		}
		
		
		fprintf(fp1,"Case #%d: %d\n",m+1,ans);

	m++;
	}
	return 0;
}
