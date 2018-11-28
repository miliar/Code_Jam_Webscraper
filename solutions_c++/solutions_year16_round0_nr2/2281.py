#include <stdio.h>
#include <iostream>
#include <cstring>
char s[200];
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf(" %s",s);
		int ans = 0;
		int la = strlen(s);
		for(int i=1;i<la;i++){
			if(s[i] != s[i-1])ans++;
		}
		if(s[la-1]=='-')ans++;
		printf("Case #%d: %d\n",cs,ans);
	}

	return 0;
}
