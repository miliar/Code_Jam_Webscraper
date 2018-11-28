#include<stdio.h>
#include<string.h>
typedef long long ll;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("filename1.txt", "w", stdout);
	ll t,n,i;
	ll b=1;
	char ar[105];
	scanf("%lld",&t);
	ll count=0;
	while(t--)
	{
		count=0;
		scanf("%s",ar);
		n=strlen(ar);
		for(i=1;i<n;i++)
		if(ar[i]!=ar[i-1])
		count++;
		if(ar[n-1]=='-')
		count++;
		printf("Case #%lld: %lld\n",b++,count);
	}
	return 0;
}
