#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <ctime>
#include <sstream>
#include <fstream>

using namespace std;

typedef long long int64;

#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define ROF(i,a,b) for(int i=(a);i>=(b);--i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())

const int N=105;

char s[N];
int64 m;

void dfs(int64 n,int64 p)
{
	if (n==0) return;
	if (p<=(1LL<<n))
	{
		s[m]='W';
		++m;
		dfs(n-1,p);
	}
	else
	{
		s[m]='L';
		++m;
		dfs(n-1,p-(1LL<<n));
	}
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("b.in","r",stdin);
		freopen("b.out","w",stdout);
	#endif

	int task;
	cin>>task;
	for (int tt=1;tt<=task;++tt)
	{
		cout<<"Case #"<<tt<<": ";
		int64 n,p;
		cin>>n>>p;
		m=0;
		dfs(n,p);
		int64 l=0,r=(1LL<<n)-1;
		while (l<r)
		{
			int64 mid=(l+r+1)/2;
			int64 j=1,k=-1,t=1LL<<(n-1),tt=1;
			while (k+j<mid)
			{
				k+=j;
				j*=2;
				tt+=t;
				t/=2;
			}
			if (tt>p) r=mid-1;
			else l=mid;
		}
		cout<<l<<' ';
		l=0,r=(1LL<<n)-1;
		while (l<r)
		{
			int64 mid=(l+r+1)/2;
			int64 j=1,k=1LL<<n,t=1LL<<(n-1),tt=1LL<<n;
			while (k-j>mid)
			{
				k-=j;
				j*=2;
				tt-=t;
				t/=2;
			}
			if (tt>p) r=mid-1;
			else l=mid;
		}
		cout<<l<<endl;
	}
	return 0;
}
