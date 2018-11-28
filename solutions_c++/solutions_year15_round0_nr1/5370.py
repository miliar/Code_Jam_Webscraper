#include<bits/stdc++.h>
using namespace std;
char s[1003];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,cse,n,i,p,o;
	scanf("%d",&T);
	for(cse=1;cse<=T;cse++)
	{
		scanf("%d%s",&n,s);
		if(s[0]=='0')p=1;else p=(int)(s[0]-'0');
		o=(int)(s[0]-'0');
		for(i=1;i<=n;i++)
		{
			if(s[i]=='0')continue;
			o+=(int)(s[i]-'0');
			if(p<i)p=i+(int)(s[i]-'0');
			else p+=(int)(s[i]-'0');
		}
		p-=o;
		if(n==0)p=(s[i]=='0'?1:0);
		printf("Case #%d: %d\n",cse,p);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
//4 00001