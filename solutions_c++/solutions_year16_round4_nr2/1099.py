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

int T,n,k,bl;
long double a[20];
long double b[20];
long double tans,ans;

long double chk()
{
	double res=0.0;
	forn(i,(1<<k))
	{
		int t=i,ko=0,kno=0;
		long double ver=1.0;
		forn(j,k)
		{
			if(t%2)
			{
				ko++;
				ver*=b[j];
			}
			else
			{
				kno++;
				ver*=(1.0-b[j]);
			}
			t/=2;
		}
		if(ko==kno)
			res+=ver;
	}
	return res;
}

int main()
{
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);
	cout <<fixed<<setprecision(15);

	cin >>T;
	forn(I,T)
	{
		cerr <<I<<endl;

		ans=0.0;

		cin >>n>>k;
		forn(i,n)
			cin >>a[i];

		forn(i,(1<<n))
		{
			int t=i;
			bl=0;
			
			forn(j,n)
			{
				if(t%2)
					b[bl++]=a[j];
				t/=2;
			}

			if(bl==k)
            	ans=max(ans,chk());
		}

		cout <<"Case #"<<I+1<<": "<<(float)ans<<endl;
	}

	return 0;
}