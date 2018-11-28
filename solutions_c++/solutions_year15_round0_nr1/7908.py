#include <bits/stdc++.h>

using namespace std;

char s[1001];

int main(int argc, char **argv)
{
	int T,t,Smax,i,standing,additional,ans;
	
	freopen("A-large.in","r",stdin);
	freopen("A-large-output.out","w",stdout);
	
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%d",&Smax);
		scanf("%s",s);
		
		standing=0;
		additional=0;
		ans=0;
		for(i=0;i<=Smax;i++)
		{
			if(standing<i) additional=(i-standing);
			else additional=0;
			standing=standing+additional+(s[i]-'0');
			ans+=additional;
		}
		
		printf("Case #%d: %d\n",t,ans);
	}
	
	return 0;
}

