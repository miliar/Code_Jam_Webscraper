#include<bits/stdc++.h>
using namespace std;
const double eps(1e-8);
const double pi(3.14159265358979);
const int N=110;
struct supply
{
	double v,c;
}s[N]={};
int n;
double v,x;
void init()
{
	cin>>n>>v>>x;
	for(int i=1;i<=n;++i)
		cin>>s[i].v>>s[i].c;
	for(int i=1;i<=n;++i)
		s[i].c-=x;
	sort(s+1,s+n+1,[](const supply &s1,const supply &s2){return s1.c<s2.c;}); 
}
void work()
{
	if(s[1].c>0 || s[n].c<0)
	{
		puts("IMPOSSIBLE");
		return;
	}
	double a=0,maxv=0;
	for(int i=1;i<=n;++i)
		a+=s[i].v*s[i].c,maxv+=s[i].v;
	int pos=1;
	while(a<-eps)
	{
		double dv=min(s[pos].v,a/s[pos].c);
		a-=dv*s[pos].c;
		maxv-=dv;
		++pos;
	}
	pos=n;
	while(a>eps)
	{
		double dv=min(s[pos].v,a/s[pos].c);
		a-=dv*s[pos].c;
		maxv-=dv;
		++pos;
	}
	printf("%.12f\n",v/maxv);
}
int main()
{	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		init();
		printf("Case #%d: ",t);
		work();
	}
	return 0;
}
