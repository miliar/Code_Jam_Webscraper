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
int arr[maxn];
char s[maxn];
using namespace std;
int main()
{
	int t,n,num,ans;
	si(t);
	for(int i=1;i<=t;i++)
	{
		ans=0;
		si(n);
		ss(s);
		for(int j=0;j<=n;j++)
		{
			arr[j]=s[j]-'0';
		}
		num=arr[0];
		for(int j=1;j<=n;j++)
		{
			if(num<j)
			{
				ans+=(j-num);
				num+=(j-num);
			}
			num=num+arr[j];
		}
		printf("Case #%d: %d\n",i,ans);

	}
	return 0;
}