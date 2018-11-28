#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
char arr[505];
int main()
{
	int i,j,k,x;
	int t,n,ans;
	freopen("B-large.in","r",stdin);
	freopen("outputi.txt","w",stdout);
	sd(t);
	for(x=1;x<=t;x++)
	{
		ss(arr);
		n=strlen(arr);
		arr[n]='+';
		arr[n+1]='\0';
		ans=0;
		for(i=1;i<=n;i++)
		{
			if(arr[i]!=arr[i-1])
				ans++;
		}
		printf("Case #%d: %d\n",x, ans);
	}
	return 0;
}