#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll func(ll n,ll k)
{
	ll ans,temp,l,i;
	ans=0;temp=1;
	while(n)
	{
		if(n%10)
		{
			ans+=temp;
		}
		temp*=k;n/=10;
	}
	l=sqrt(ans);
	for(i=2;i<=l;i++)
	{
		if(!(ans%i))
		{
			return i;
		}
	}
	return 0;
}
ll bin(ll n)
{
	ll temp,j,b[100],i=0,q;
	q=n;
	while(q)
	{
		b[i++]=q%2;q/=2;
	}
	temp=0;
	for(j=0;j<i;j++)
	{
		if(b[j])
		temp+=pow(10,j);
	}
	return temp;
}
int main()
{
	ll t,cs,n,j,i,idx,s,st,temp,k,x,cnt;
	ll a[10];
	scanf("%lld",&t);
	for(cs=1;cs<=t;cs++)
	{
		scanf("%lld %lld",&n,&j);
		cnt=0;
		printf("Case #%lld:\n",cs);
		s=pow(2,n-2);
		st=pow(10,n-1)+1;
		for(i=0;i<s;i++)
		{
			temp=st+bin(i)*10;
			idx=0;
			for(k=2;k<11;k++)
			{
				x=func(temp,k);
				if(!x) break;
				a[idx]=x;idx++;
			}
			if(!x) continue;
			printf("%lld ",temp);
			for(idx=0;idx<9;idx++)
			{
				printf("%lld ",a[idx]);
			}
			printf("\n");
			cnt++;
			if(cnt==j) break;
		}
	}
}
