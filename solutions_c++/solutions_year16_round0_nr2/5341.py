#include<bits/stdc++.h>
using namespace std;


int main()
{
	int t,ans;
	char s[1002],c;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		ans=0;
		scanf("%s",s);
		c=s[0];
		for(int j=1;j<strlen(s);j++)
		{
		if(s[j]!=c)
		ans+=1,c=s[j];
		}
		if(c=='-')
		ans++;
		printf("Case #%d: %d\n",i,ans);
	}
}
