#include<bits/stdc++.h>

using namespace std;

int T,n,a[1010];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",a+i);
		int ma=*max_element(a,a+n);
		int ans=ma;
		for(int eat=1;eat<=ma;eat++)
		{
			int cur=eat;
			for(int i=0;i<n&&cur<ans;i++)
				cur+=(a[i]-1)/eat;
			if (cur<ans) ans=cur;
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}