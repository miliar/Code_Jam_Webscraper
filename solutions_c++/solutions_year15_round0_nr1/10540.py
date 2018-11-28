#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,i=0,flag=0,p=1,b=0,ans=0,c=1;
	scanf("%d",&t);
	while(t--)
	{	b=0,ans=0,flag=0;
		scanf("%d",&n);
		char a[n+1];
		scanf("%s",a);
		//puts(a);
		b=a[0]-'0';
		for(i=1;i<n+1;i++)
		{
			if(i>b)
			{
				ans+=(i-b);
				b+=(i-b);
			}
			b+=(a[i]-'0');
		}
		printf("Case #%d: %d\n",c,ans);
		ans=b=0;
		c++;
	}
	return 0;
}
