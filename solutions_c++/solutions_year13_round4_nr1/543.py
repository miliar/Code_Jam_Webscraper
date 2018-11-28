#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int u=10010;
struct rec{int x,y,z;}a[u];
bool operator <(rec a,rec b)
{
	return a.x<b.x||a.x==b.x&&a.y>b.y;
}
long long sqr(long long x,long long y)
{
	return x==y?0:(y-x)*(y-x-1)/2;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int n,m,t,T,i,j;
	long long ans,tot;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n>>m;
		for(i=1,ans=tot=0;i<=m;i++)
		{
			cin>>a[i].x>>a[i].y>>a[i].z;
			tot+=sqr(a[i].x,a[i].y)*a[i].z;
		}
		for(i=m;i;i--)
			for(j=1;j<a[i].z;j++) a[++m]=a[i];
		sort(a+1,a+m+1);
		for(i=1;i<m;i++)
			for(j=i+1;j<=m;j++)
				if(a[i].y<a[j].x) break;
				else if(sqr(a[i].x,a[i].y)+sqr(a[j].x,a[j].y)<sqr(a[i].x,a[j].y)+sqr(a[j].x,a[i].y)) swap(a[i].y,a[j].y);
		for(i=1;i<=m;i++) ans+=sqr(a[i].x,a[i].y);
		cout<<"Case #"<<t<<": "<<ans-tot<<endl;
	}
}
