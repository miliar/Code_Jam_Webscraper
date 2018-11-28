#include<iostream>
using namespace std;

long long n,m,o[5000],e[5000],p[5000],a[5000],b[5000],h[5000];
long long mo=1000002013;
long long inf=1000002013;
long long res,num,Testnum,numb;
int mid;

long long f(long long x)
{
	res=(((2ll*n+1)%mo*x)%mo-(x*x)%mo)%mo;
	res=(res+mo)%mo;
	if (res%2==0) res/=2;
    else res=(res+mo)/2;
    return res;
}

int work(int x)
{
    int l=0,r=num+1;
	while (l+1<r)
	{
		mid=(l+r)/2;
		if (a[mid]<=x)  l=mid; else r=mid;
	}
	return l;
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	cin>>Testnum;
	for (int test=1; test<=Testnum; ++test)
	{
		cin>>n>>m;
		memset(a,0,sizeof a);
		num=0;
		long long ans=0;
		for (int i=1; i<=m; i++)
		{
			cin>>o[i]>>e[i]>>p[i];
			a[++num]=o[i]; a[++num]=e[i];
			ans=(ans+(f(e[i]-o[i])*p[i]))%mo;
		}
		sort(a+1,a+num+1);
		a[0]=-1; numb=0;
		for (int i=1; i<=num; i++) if (a[i]!=a[i-1]) b[++numb]=a[i];
		num=numb;
		for (int i=0; i<=5000; i++) a[i]=b[i];
		memset(h,0,sizeof h);
		for (int i=1; i<=m; i++)
		{
			int oo=work(o[i]),ee=work(e[i]);
			for (int j=oo; j<ee; j++) {h[j]+=p[i]; h[j]%=mo;}
		}
		long long last=-1,len=0,tinf=mo,tres=0;
		int k=1;
		while (k>0)
		{
		    k++;
			for (int i=1; i<=num; i++)
			{
				if (h[i]>0)
				{
					if (last==-1) last=i;
					len+=a[i+1]-a[i];
					tinf=min(tinf,h[i]);
				}
				if (h[i]==0 && last!=-1)
				{
					tres=(tres+(f(len)*tinf))%mo;
					for (int j=last; j<i; j++) h[j]-=tinf;
					last=-1; len=0; tinf=inf;
				}
			}
			bool ok=false;
			for (int i=1; i<=num; ++i) if (h[i]>0) ok=true;
			if (!ok) break;
		}
		cout<<"Case #"<<test<<": "<<(ans-tres+mo)%mo<<"\n";
	}
	return 0;
}
