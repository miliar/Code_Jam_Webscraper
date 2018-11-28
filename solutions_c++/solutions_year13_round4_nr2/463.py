
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int cases,n;
long long a,b,num,p,t,pp;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	cin>>cases;
	for(int i=0;i<cases;++i)
	{
		cin>>n>>p;
		num=(long long)1<<n;
		if(p==num)cout<<"Case #"<<i+1<<": "<<num-1<<" "<<num-1<<endl;
		else
		{
			a=0;
			t=num;
			int j=0;
			pp=p;
			while(pp>(t>>=1))
			{
				++j;
				pp-=t;
				a|=(long long)1<<j;
			}
			b=num-2;
			t=num;
			pp=num-p;
			j=0;
			while(pp>(t>>=1))
			{
				++j;
				pp-=t;
				b^=(long long)1<<j;
			}
			cout<<"Case #"<<i+1<<": "<<a<<" "<<b<<endl;
		}
	}
}