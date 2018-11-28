#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
char str[11111];
int main()
{
	int T,cas=0;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%s",str);
		int len=strlen(str);
		int ans=0;
		for(int i=1;i<len;i++)
		{
			if(str[i]!=str[i-1])ans++;
		}
		if(str[len-1]=='-')ans++;
		printf("Case #%d: %d\n",++cas,ans);
	}
}