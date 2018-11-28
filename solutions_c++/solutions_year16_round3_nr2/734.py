#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

#define N 50

using namespace std;

unsigned long long int c[N+1];
int d[N+1];
int main()
{
	int i,j,k;
	int b;
	int t;
	int e;
	unsigned long long int m;
	for(i=1,c[0]=1;i<=N;i++)
	{
		c[i]=c[i-1]*2;
	}
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>b>>m;
		cout<<"Case #"<<k<<": ";
		if(c[b-2]<m)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		cout<<"POSSIBLE"<<endl;
		if(c[b-2]==m)
		{
			e=1;
			for(i=0;i<b;i++)
			{
				d[i]=1;
			}
		}
		else
		{
			e=0;
			memset(d,0,sizeof(d));
			for(i=0;i<N;i++)
			{
				if(!m)
					break;
				if(m%2==1)
				{
					d[i]=1;
				}
				m=m/2;
			}
		}
		for(i=0;i<b;i++)
		{
			for(j=0;j<=i;j++)
			{
				cout<<"0";
			}
			for(j=i+1;j<b-1;j++)
			{
				cout<<"1";
			}
			if(i<b-1)
			{
				if(!i && e)
					cout<<"1";
				else if(i && d[i-1])
					cout<<"1";
				else
					cout<<"0";
			}
			cout<<endl;
		}
	}

	return 0;
}
