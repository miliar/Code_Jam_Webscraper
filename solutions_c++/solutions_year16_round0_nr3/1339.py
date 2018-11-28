#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

const long long MAXM=1000007;
const long long MAXN=1007;
const long long MAXT=507;

long long i,j,k,n,m,t,x,y,tcase,mbit,cnta;
long long ans[MAXT][17];
bool isPrime[MAXM];
long long p[MAXN];
long long cnt;

void calPrime()
{
	cnt=0;
	memset(isPrime,-1,sizeof(isPrime));
	isPrime[0]=0;
	isPrime[1]=0;
	for (i=2;i<MAXN;i++)
	{
		if (isPrime[i])
		{
			for (j=i+i;j<MAXM;j+=i)
			{
				isPrime[j]=0;
			}
		}
	}
	for (i=2;i<MAXN;i++)
	{
		if (isPrime[i])
		{
			p[cnt++]=i;
		}
	}
	// cout<<"long long p["<<cnt<<"]={"<<p[0];
	// for (i=1;i<cnt;i++)
	// 	cout<<","<<p[i];
	// cout<<"};"<<endl;
}

bool ok(long long bit,long long k)
{
	long long i,j,x,t;
	x=1;
	for (i=1;i<n-1;i++)
	{
		t=bit%2;
		bit/=2;
		x=x*k+t;
	}
	x=x*k+1;
	if (k==10)
	{
		ans[cnta][0]=x;
	}
	for (i=0;i<cnt;i++)
	{
		if (p[i]>=x)
		{
			return false;
		}
		if (x%p[i]==0)
		{
			ans[cnta][k]=p[i];
			return true;
		}
	}
	return false;
}

void test(long long bit)
{
	long long i;
	for (i=2;i<=10;i++)
	{
		if (!ok(bit,i))
		{
			return;
		}
	}
	cnta++;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	calPrime();
	cin>>tcase;
	while (tcase--)
	{
		cout<<"Case #1: "<<endl;
		cnta=0;
		cin>>n>>m;
		mbit=(1LL<<(n-2));
		for (i=0;i<mbit;i++)
		{
			test(i);
			if (cnta>=m)
			{
				break;
			}
		}
		for (i=0;i<m;i++)
		{
			cout<<ans[i][0];
			for (j=2;j<=10;j++)
			{
				cout<<" "<<ans[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}

