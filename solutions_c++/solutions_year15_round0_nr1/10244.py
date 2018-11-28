#include<stdio.h>
main()
{
	int t,n,s,frnd,i,j,l;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		s=0;
		frnd=0;
		scanf("%d",&n);
		char shy[n];
		scanf("%s",shy);
		s=shy[0]-48;
		for(i=1;shy[i]!='\0';i++)
		{
			
			if(i>s&& shy[i]!='0')
			{
			   	frnd=frnd+i-s;
			   	s=frnd+s;
			}
			s=s+shy[i]-48;
		}
		printf("Case #%d: %d",j,frnd);
	   	
	}
}
