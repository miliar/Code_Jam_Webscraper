#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
char s[1000+10];
int k;
char flip(char c)
{
	if(c=='+')return '-';
	else return '+';
}
bool check(char *s,int len)
{
	for(int i=0;i<len;i++)
		if(s[i]!='+')return false;
	return true;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		scanf("%s %d",s,&k);
		int len=strlen(s);
		int ans=0;
		for(int i=0;i+k-1<len;i++)
		{
			if(s[i]=='+')continue;
			ans++;
			for(int j=0;j<k;j++)s[i+j]=flip(s[i+j]);
		}
		if(check(s,len))printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}