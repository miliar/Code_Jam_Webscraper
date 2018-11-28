#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
int n,a[10000];
int main()
{
	int T;
	scanf("%d",&T);
	for(int tcase=1;tcase<=T;tcase++)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)scanf("%d",&a[i]);
		int ans=0;
		while(n)
		{
			int t=1;
			for(int j=1;j<=n;j++)
			{
				if(a[j]<a[t])t=j;
			}
			ans+=min(t-1,n-t);
			for(int i=t+1;i<=n;i++)swap(a[i],a[i-1]);
			n--;
		}
		printf("Case #%d: %d\n",tcase,ans);
	}
}