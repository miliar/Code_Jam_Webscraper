#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		char s[1005];
		long int len,sum=0,n;
		scanf("%ld%s",&n,s);
		len=n+1;
		int tot=s[0]-'0';
		for(int i=1;i<len;i++)
		{
				int np=s[i]-'0';
				if(i>tot && np!=0)
				{sum+=i-tot;tot+=i-tot;}
				
				tot+=np;
				//cout<<i<<":"<<s[i]<<":"<<sum<<":"<<tot<<endl;
		}
		printf("case #%d: %ld\n",j,sum);
	}
	return 0;
}