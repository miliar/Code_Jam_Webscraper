#include<bits/stdc++.h>
using namespace std;

char a[1005];

int main()
{freopen("E:/in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,t,n,i,c,s;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%d%s",&n,a);
		for(s=c=i=0;i<=n;i++)
			if(a[i]=='0')
			{
				if(c<=i)
					c++,s++;
			}
			else
				c+=a[i]-'0';
		printf("Case #%d: %d\n",t,s);
	}
	return 0;
}
