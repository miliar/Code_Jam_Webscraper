#include <bits/stdc++.h>
int main(int argc, char const *argv[])
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int smax;
		scanf("%d",&smax);
		char s[smax+1];
		scanf("%s",s);
		int res=0,count=0,tmp,flag=0;
		for(int i=0;i<strlen(s);i++)
		{
			if(s[i]=='0')
				continue;
			if(i>count)
			{
				tmp=i-count;
				res+=tmp;
				count+=(s[i]-'0')+tmp;
			}
			else
			{
				count+=(s[i]-'0');
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}