#include<bits/stdc++.h>
using namespace std;
const int N=1010,K=110,Inf=1<<29;
int n,k,s[N]={},a[K]={},b[K]={};
void init()
{
	cin>>n>>k;
	for(int i=1;i<=n-k+1;++i)
		cin>>s[i];
	for(int i=1;i<=k;++i)
	{
		a[i]=0;
		b[i]=0;
		for(int j=i,t=0;j<=n-k;j+=k)
		{
			t+=s[j+1]-s[j];
			a[i]=min(a[i],t);
			b[i]=max(b[i],t);
		}
		//cerr<<"i="<<i<<" l="<<a[i]<<" r="<<b[i]<<endl;
	}
}
bool check(int maxd)
{
	long long l=0,r=0;
	for(int i=1;i<=k;++i)
	{
		l+=a[i];
		r+=maxd-b[i];
	}
	l=s[1]+l,r=s[1]-r;
	if(l>r) swap(l,r);
	if(l<=0 && 0<=r)
		return true;
	if(l>0 && r<0)
		return false;
	l=abs(l),r=abs(r);
	if(l>r) swap(l,r);
	l=(l+k-1)/k,r=r/k;
	//cerr<<"l="<<l<<" r="<<r<<endl;
	return l<=r;
}
void work()
{
	int l=0,r=Inf;
	for(int i=1;i<=k;++i)
		l=max(l,b[i]-a[i]);
	//cerr<<"l="<<l<<" r="<<r<<endl;
	while(l!=r)
	{
		int mid=(l+r)>>1;
		if(check(mid))
			r=mid;
		else
			l=mid+1;
	}
	check(l);
	cout<<l<<endl;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		init();
		cout<<"Case #"<<t<<": ";
		work();
	}
	return 0;
}
