#include<bits/stdc++.h>
using namespace std;
main()
{
	freopen("A-large.in","r",stdin);
	freopen("Out-A-large.txt","w",stdout);
	int a,b,c,d,e,ans;
	char s[2000];
	scanf("%d",&a);
	for(b=0;b<a;b++)
	{
		scanf("%d %s",&c,s);
		e=0;
		ans=0;
		for(d=0;d<=c;d++)
		{
			if(s[d]!='0')
			{
				if(e<d)ans+=d-e,e=d;
				e+=s[d]-'0';
			}
		}
		printf("Case #%d: %d\n",b+1,ans);
	}
}
