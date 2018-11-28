#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
using namespace std;
int T,n,m,s;
int calc(int x)
{return x?1<<x%10|calc(x/10):0;}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>n;
		cout<<"Case #"<<i<<": ";
		if(n==0)cout<<"INSOMNIA"<<endl;
		else
		{
			for(m=s=0;s!=1023;)
				s|=calc(m+=n);
			cout<<m<<endl;
		}
	}
	return 0;
}

