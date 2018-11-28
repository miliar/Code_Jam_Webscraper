#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char s[1005];
int main()
{
	int T,t,len,ans;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%s",&s);
		printf("Case #%d: ",t);
		len=strlen(s);
		if (s[len-1]=='+') ans=0;
		else ans=1;
		for (int i=0;i<len-1;i++)
			if (s[i]!=s[i+1]) ans++;
		printf("%d\n",ans);
	}
	return 0;
} 
