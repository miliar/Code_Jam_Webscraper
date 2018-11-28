#include<bits/stdc++.h>
using namespace std;
int a[1005];
int main()
{
	int T,n;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d", &n);
		
		for(int i=0; i<n; i++)
		scanf("%d", &a[i]);
		
		int ans1=0;
		for(int i=0; i<n-1; i++)
		{
			if(a[i]>a[i+1])
			ans1+=(a[i]-a[i+1]);
		}
		
		int ans2=0;
		
		int mx=-1;
		for(int i=0; i<n-1; i++)
		{
			if((a[i]-a[i+1]>0) && (a[i]-a[i+1]>mx))
			mx=a[i]-a[i+1];
		}
		
		if(mx<0)
		mx=0;
		
		for(int i=0; i<n-1; i++)
		{
			if(a[i]>=mx)
			ans2+=mx;
			else
			ans2+=a[i];
		}
		printf("Case #%d: %d %d\n", t, ans1, ans2);
	}
	return 0;
}
