#include<cstdio>
#include<iostream>
using namespace std;
long long mo=1000002013;
long long inf=1000002013;
long long n,m,u[3333],v[3333],w[3333],a[3333],b[3333],h[3333];
long long num,T,numb;

int binary(int x)
{
	int l=0,r=num+1,mid;
	while (l+1<r)
	{
		mid=(l+r)/2;
		if (a[mid]<=x)
			l=mid;
		else
		 	r=mid;
	}
	return l;
}

long long calc(long long x)
{
	long long res=(-(x*x)%mo+((2*n+1)%mo*x)%mo)%mo;
	res=(res+mo)%mo;
	if (res%2==0)
		return res/2;
	return (res+mo)/2;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>T;
	for (int tt=1; tt<=T; tt++)
	{
		cin>>n>>m;
		memset(a,0,sizeof a);
		num=0;
		long long ans=0;
		for (int i=1; i<=m; i++)
		{
			cin>>u[i]>>v[i]>>w[i];
			a[++num]=u[i]; a[++num]=v[i];
			ans+=(calc(v[i]-u[i])*w[i])%mo;
			ans%=mo;
		}
		sort(a+1,a+num+1);
		a[0]=-1;
		numb=0;
		for (int i=1; i<=num; i++)
			if (a[i]!=a[i-1])
				b[++numb]=a[i];
		num=numb;
		memcpy(a,b,sizeof b);
		memset(h,0,sizeof h);
		for (int i=1; i<=m; i++)
		{
			int uu=binary(u[i]),vv=binary(v[i]);
			for (int j=uu; j<vv; j++)
			{
				h[j]+=w[i]; h[j]%=mo;
			}
		}
		long long lst=-1,len=0,mw=inf,ans1=0;
		for (int k=1; k>0; k++)
		{
			for (int i=1; i<=num; i++)
			{
				if (h[i]>0)
				{
					if (lst==-1)
						lst=i;
					len+=a[i+1]-a[i];
					mw=min(mw,h[i]);
				}
				if (h[i]==0 && lst!=-1)
				{
					ans1+=(calc(len)*mw)%mo;
					ans1%=mo;
					for (int j=lst; j<i; j++)
						h[j]-=mw;
					lst=-1; len=0; mw=inf;
				}
			}
			bool ok=false;
			for (int i=1; i<=num; i++)
				if (h[i]>0) ok=true;
			if (!ok) break;
		}
		cout<<"Case #"<<tt<<": ";
		cout<<(ans-ans1+mo)%mo<<"\n";
	}
	return 0;
}