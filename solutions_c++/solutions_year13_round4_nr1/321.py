#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#define mod 1000002013
using namespace std;
long long n;
long long x[1010],y[1010],p[1010];
map <long long,long long> M;
long long xx[2020];
long long val[2020];
int run;
struct yo
{
	long long a,num;
	bool operator < (const yo &tt) const
	{
		return a<tt.a;
	}
}A[1010],B[1010];
long long f(long long xx,long long yy)
{
	return ((n*(n+1)/2-(n-xx)*(n-xx+1)/2)%mod)*yy%mod;
}
main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,m,k,pp,q;
	long long ans1,ans2;
	cin >> t;
	long long z,zz,ans;
	std::map<long long,long long>::iterator it;
	long long MIN;
	int zzz;
	for(int ll=0;ll<t;ll++)
	{
		M.clear();
		ans1=0ll;
		scanf("%lld %d",&n,&m);
		for(int i=1;i<=m;i++)
		{
			scanf("%lld %lld %lld",&x[i],&y[i],&p[i]);
			z=y[i]-x[i];
			ans1+=f(y[i]-x[i],p[i]);
			ans1%=mod;
		}
		for(int i=1;i<=m;i++)
		{
			M[x[i]]+=p[i];
			M[y[i]]-=p[i];
		}
		run=0;
		ans2=0ll;
		for(it=M.begin();it!=M.end();it++)
		{
			xx[run]=it->first;
			val[run++]=it->second;
		}
		for(int i=1;i<run;i++) val[i]+=val[i-1];
		/*for(int i=0;i<run;i++) 
		{
			cout << "---" << xx[i] << " " << val[i] << endl;
		}*/
		for(int i=0;i<run;)
		{
			if(val[i]==0)
			{
				i++;
				continue;
			}
			MIN=2000000000ll*2000000000ll;
			for(int j=i;j<run;j++)
			{
				zzz=j;
				if(val[j]==0) break;
				MIN=min(MIN,val[j]);
			}
			//cout << "aaaa" << xx[i] << " " << xx[zzz] << " " << MIN << endl;
			ans2+=f(xx[zzz]-xx[i],MIN);
			ans2%=mod;
			for(int j=i;j<zzz;j++) val[j]-=MIN;
		}
		ans=ans1-ans2;
		//cout << ans1 <<" "  << ans2 << endl;
		printf("Case #%d: ",ll+1);
		printf("%lld\n",((ans%mod)+mod)%mod);
	}
}
/*
3
6 2
1 3 1
3 6 1
6 2
1 3 2
4 6 1
10 2
1 7 2
6 9 1
*/
