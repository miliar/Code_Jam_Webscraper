#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define forn(i, n) for(int i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;

int N,n,ans,mmax,mmax2,t,kol;
int a[1010];

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);

	cin >>N;
	forn(I,N)
	{
		forn(i,1010)
			a[i]=0;

		cin >>n;
		forn(i,n)
		{
			cin >>t;
			a[t]++;
		}

		ans=999999;
		int ind=-1;
		for(int i=1; i<1001; i++)
		{
			t=0;
			for(int j=i+1; j<1001; j++)
				t+=((j-1)/i)*a[j];
			if(i+t<ans)
			{
				ans=i+t;
				ind=i;
			}
		}
		//cerr <<I<<' '<<ind<<' '<<ans<<endl;
		/*
		for(ans=0; ; ans++)
		{
			mmax=0;
			mmax2=0;

			for(int i=1000; i>0; i--)
				if(a[i]>0)
				{
					if(mmax==0)
						mmax=i;
					else if(mmax2=0)
						mmax2=i;
				}
			if(mmax==0)
				break;
			t=mmax/2+mmax%2;
			if(a[mmax]+max(t,mmax2)<mmax)
			{
				a[mmax/2]+=a[mmax];
				a[mmax/2+mmax%2]+=a[mmax];
				a[mmax]=0;
			}
			else
			{
				forn(i,1000)
					a[i]=a[i+1];
				a[0]=0;
			}	
		}
		*/
		cout <<"Case #"<<I+1<<": "<<ans<<endl;
	}

	return 0;
}
