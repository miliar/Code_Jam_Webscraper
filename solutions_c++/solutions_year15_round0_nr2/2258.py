#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define ll long long
#define mod 1000000007
#define pb(n) push_back(n)
#define maxn 1005
using namespace std;
int arr[maxn];
int main()
{
	int t,n;
	si(t);
	for(int l=1;l<=t;l++)
	{
		si(n);
		for(int i=0;i<n;i++)
			si(arr[i]);
		int ans=1005;
		int tempans=0;
		for(int i=1;i<=1000;i++)
		{
			tempans=i;
			for(int j=0;j<n;j++)
			{
				tempans+=(arr[j]-1)/i;
			}
			ans=min(ans,tempans);
		}
		printf("Case #%d: %d\n",l,ans);
	}
	return 0;
}