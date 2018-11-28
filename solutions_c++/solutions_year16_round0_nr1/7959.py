#include<bits/stdc++.h>
using namespace std;
#define for1(i,n) for(i=0;i<n;i++)
#define for2(i,n) for(i=n-1;i>=0;i--)
#define ll long long int
#define CLEAR(array, value) memset(array, value, sizeof(array));
#define si(a)     scanf("%d", &a)
#define sl(a)     scanf("%lld", &a)
#define sc(a)     scanf(" %c", &a)
#define ss(a)     scanf("%s", a)
#define pi(a)     printf("%d\n", a)
#define pl(a)     printf("%lld\n", a)
#define pn        printf("\n")

#define mod long(1e9+7)
int check_a(bool a[],ll n)
{
	int i,j,count=0;
	while(n>0)
	{
		a[n%10]=true;
		n/=10;
	}
	for(i=0;i<=9;i++)
	{
		if(a[i]==true)
		count++;
	}
	if(count==10)
	return 1;
	else
	return 0;
}
int	main()
{
   // freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
	ll t,j,k,ans=0;
	sl(t);
	for(j=1;j<=t;j++)
	{
		ll n;
		bool check[10]={false};
		sl(n);
		int i=1;
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",j);

		}
		else
		while(1)
		{
			k=i*n;
			if(check_a(check,k)==1)
			{
				printf("Case #%lld: %lld\n",j,k);
				break;
			}
			else
			i++;
		 }
	}
	return 0;
}
