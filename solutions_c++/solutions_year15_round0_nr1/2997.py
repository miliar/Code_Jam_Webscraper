#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int teskes,n;
	scanf("%d",&teskes);
	for(int tc=1;tc<=teskes;tc++)
	{
		char arr[1005];
		scanf("%d",&n);
		scanf("%s",arr);
		
		int ans=0;
		int punya=0;
		for(int x=0;x<=n;x++)
		{
			if(arr[x]!='0')
			{
				if(punya<x)
				{
					ans+=(x-punya);
					punya=x;
					punya+=arr[x]-'0';
				}
				else
				{
					punya+=arr[x]-'0';
				}
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	
	return 0;
}
