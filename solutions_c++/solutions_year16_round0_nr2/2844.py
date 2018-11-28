#include <iostream>
#include <cstdio>
#include <cstring>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,t;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		int i,ans=0;
		char s[1010];
		scanf("%s",s);
		for (i=0;s[i]=='-'&&s[i];i++);
		if (i!=0) ans++;
		for (;s[i];i++)
		{
			if (s[i-1]=='+'&&s[i]=='-') ans+=2;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
