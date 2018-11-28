#include <bits/stdc++.h>
#define ll long long
#define mylim 1000010
using namespace std;
bool mycheck(ll int,ll int);
bool myconvert(ll int);
bool works();
ll int v[12];
ll int a[40],till;
bool p[mylim];
ll int pr[mylim];
ll int n,m;
bool works()
{
	bool flag=1;
	ll int i;
	for(i=2;i<=10;i++)
	{
		if(!myconvert(i))
		{
			flag=0;
			break;
		}
	}
	return flag;
}
bool myconvert(ll int index)
{
	ll int x=0,i,b=1;
	for(i=(n-1);i>=0;i--)
	{
		x+=b*a[i];
		b*=index;
	}
	return mycheck(x,index);
}
bool mycheck(ll int x,ll int index)
{
	ll int i;
	bool flag=0;
	for(i=0;i<till;i++)
	{
		if(x>pr[i] && (x%pr[i])==0)
		{
			v[index]=pr[i];
			flag=1;
			break;
		}
	}
	return flag;
}
int main()
{
	//~ ios_base::sync_with_stdio(false);
	//~ cin.tie(NULL);
	//Generate all primes till 10^6
	memset(p,0,sizeof(p));
	ll int i,j;
	p[0]=1;p[1]=1;
	for(i=2;(i*i)<mylim;i++)
	{
		if(p[i])
		continue;
		for(j=2;(j*i)<mylim;j++)
		{
			p[j*i]=1;//Not prime
		}
	}
	 j=0;
	for(i=0;i<mylim;i++)
	{
		if(p[i]==0)
		pr[j++]=i;
	}
	till=j;
	//cout<<j<<endl;//78499
	//for small atleast
	ll int test,t;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		printf("Case #%lld:\n",t);
		cin>>n>>m;
		memset(a,0,sizeof(a));
		a[0]=1;a[n-1]=1;
		for(i=0;;i++)
		{
			for(j=(n-2);j>=0;j--)
			{
				a[j]=(a[j]+1)%2;
				if(a[j])
				break;
			}
			if(works())
			{
				for(j=0;j<n;j++)
				cout<<a[j];
				cout<<" ";
				for(j=2;j<=10;j++)
				cout<<v[j]<<" ";
				cout<<endl;
				m--;
			}
			if(m==0)
			break;
		}
	}
	return 0;
}
