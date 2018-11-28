#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int t,j,i,s,n,r,count,test;
	scanf("%d",&test);
	for(j=1;j<=test;j++)
	{
		scanf("%d %d",&r,&t);
		s=0;
		count=0;
		while(s<=t)
		{
			s=s+(1+2*r);
			r+=2;	
			if(s<=t)
				count++;
		}
		printf("Case #%d: %d\n",j,count);
	}
	return 0;
}
		
		
		
