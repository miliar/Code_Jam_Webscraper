#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main()
{
	int t,j,max,i,cnt,ans;
	char str[10000];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%d",&max);
		scanf("%s",&str);
		
		ans=0;     cnt=str[0]-'0';
		
		for(i=1;i<=max;i++)
		{	
			if( cnt >=i)   cnt+=str[i]-'0';
			else	  {  ans+=(i-cnt);  cnt+=(i-cnt)+str[i]-'0';	}
					//cout<<ans<<endl;
		}
		
		printf("Case #%d: %d\n",j,ans);
		cnt=0;
	}
	return 0;
}