#include <cstdio>
#include <iostream>

using namespace std;

long long n;
int T;
long long p;
long long getMax(long long t)
{
	long long tot = 1<<n;
	long long smaller = tot-1-t;
	long long ans = 0;
	long long tt = 0;
	while (smaller>0)
	{
		ans = ans<<1;
		++tt;
		smaller --;
		smaller>>=1;
	}
	for (long long i = 0; i<n-tt;++i)
	{
		ans = ans <<1;
		ans = ans+1;
	}
	return ans;
}
long long getMin(long long t)
{
	long long tot = 1<<n;
	long long smaller = t;
	long long ans = 0;
	long long tt = 0;
	while (smaller>0)
	{
		ans = ans<<1;
		ans = ans+1;
		++tt;
		smaller--;
		smaller>>=1;
	}
	for (long long i = 0; i<n-tt;++i)
		ans = ans <<1;
	return ans;
}
int main()
{
	cin>>T;
	for (int I=1;I<=T;++I)
	{
		cin>>n>>p;
		//cout<<"OK"<<endl;
		
		long long L = 0, R = (1<<n)-1;
		while (L<R)
		{
			long long MID = (L+R+1)/2;
			if (getMin(MID)>=p)
				R=MID-1;
			else
				L=MID;
			//cout<<L<<' '<<R<<endl;
		}
		cout<<"Case #"<<I<<": "<<L<<' ';
		L=0, R=(1<<n)-1;
		while (L<R)
		{
			long long MID = (L+R+1)/2;
			if (getMax(MID)>=p)
				R=MID-1;
			else
				L=MID;
		}
		cout<<L<<endl;
	}
}
