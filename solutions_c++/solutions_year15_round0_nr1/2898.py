#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (int tt = 1; tt<=t; ++tt)
	{
		int n,sum = 0,ans = 0;
		scanf("%d",&n);
		char ch = getchar();
		for (int i=0; i<=n; ++i)
		{
			ch = getchar();
			int now = ch-'0';
		//	cout<<now<<endl;
			if (now != 0)
			{
				if (sum<i) 
				{
					ans += i -sum;
					sum = i;
				}
				sum += now;	
			}
		}
		printf("Case #%d: %d",tt,ans);
		if (t!=tt) printf("\n");
	}
	return 0;
}
