#include<bits/stdc++.h>
using namespace std;
char s[2005];
int a[2005];
int main()
{
	int t,j;
	scanf("%d",&t);
	for(j=1;j<=t;j++){
		int smax,i,ans=0,count=0;
		scanf("%d",&smax);
		scanf("%s",s);
		for(i=0;i<=smax;i++)
		a[i]=s[i]-'0';
		count = a[0];
		for(i=1;i<=smax;i++)
		{
			if(count<i)
			{	
				ans+=i-count;
				count+=(i-count);
			}
			count+=a[i];
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}

