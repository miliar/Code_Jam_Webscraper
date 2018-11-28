#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)   for(i=a;i>=b;i--)
# define toint(n)   (n-'0')
typedef long long ll;

ll Solve1(int  n, int a[])
{
	ll ans=0,i,temp;
	fo(i,0,n-1)
	{
		temp=a[i]-a[i+1];
		if(temp>0)
			ans+=temp;
	}
	return ans;
}

ll Solve2(int n, int a[])
{
	int ans=0,i,temp;
	ll final=0;
	fo(i,0,n-1)
	{
		temp=a[i]-a[i+1];
		if(temp>ans)
			ans=temp;
	}
	fo(i,0,n-1)
	{
		if(a[i]-ans>0)
			final+=ans;
		else
			final+=a[i];
		//printf("%lld\n",final );
	}
	return final;
}

int main(int argc, char const *argv[])
{
	//freopen("A-large.in-2.in","r",stdin);
    //freopen("A-large.in-2.out","w",stdout);
	int t,n,i,a[1001],k;
	ll ans1,ans2;
	s(t);
	fo(k,1,t+1)
	{
		s(n);
		fo(i,0,n)
			s(a[i]);
		ans1=Solve1(n,a);
		ans2=Solve2(n,a);

		printf("Case #%d: %lld %lld\n",k,ans1, ans2);
	}
	return 0;
}