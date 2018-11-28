#include<bits/stdc++.h>
using namespace std;
const int N=10010,S=66,M=1050000;
int n,m,tot=0,p[N]={},t[N]={},s[M]={},del[M]={},now=0,ans[S]={};
void init()
{
	tot=m=0;
	cin>>n;
	for(int i=1;i<=n;++i)
		cin>>p[i];
	for(int i=1;i<=n;++i)
		cin>>t[i];
	for(int i=1;i<=n;++i)
		while(t[i]--)
			s[++m]=p[i];
	sort(s+1,s+m+1);
}
void get_element()
{
	++now;
	ans[++tot]=s[m]-s[m-1];
	multimap<int,int> num;
	for(int i=1;i<=m;++i)
		num.insert({s[i],i});
	for(int i=m;i>=1;--i)
	{
		auto it=num.find(s[i]+ans[tot]);
		if(it!=num.end())
		{
			del[it->second]=now;
			num.erase(it);
			num.erase(num.find(s[i]));
		}
	}
	int pos=0;
	for(int i=1;i<=m;++i)
		if(del[i]!=now)
			s[++pos]=s[i];
	m=pos;
}
void work()
{
	while(m!=1)
		get_element();
	sort(ans+1,ans+tot+1);
	for(int i=1;i<tot;++i)
		cout<<ans[i]<<' ';
	cout<<ans[tot]<<endl;
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
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
