#include <stdio.h>

#include <string.h>
#include <vector>
#include <map>
#include <stack>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

#define ll long long
#define sf scanf
#define pf printf
#define pb push_back
#define clr(x) memset(x,0,sizeof(x))
#define fr(x,a,b) for(int x=a; x<b;++x)


int dp1[10000], dp2[10000];
int a[10000];

int main()
{
	int T;
	sf("%d",&T);
	fr(ca,0,T)
	{
		int n;
		sf("%d",&n);
		fr(i,0,n)
		{
			sf("%d",&a[i]);
		}

		clr( dp1 );
		clr( dp2 );
		dp1[0] = 0;
		fr(i,1,n)
		{
			int x = 0;
			fr(j,0,i)
			{
				if( a[j] > a[i] )
				{
					x++;
				}
			}
			dp1[i] = dp1[i-1] + x;
//			pf("%d dp1 = %d\n",a[i], dp1[i]);
		}

		dp2[n-1] = 0;
		for( int i = n-2; i >= 0; --i )
		{
			int x = 0;
			for( int j = n-1; j > i; --j )
			{
				if( a[j] > a[i] )
				{
					x++;
				}
			}
			dp2[i] = dp2[i+1] + x;
		}

		int ans = dp2[0];
		for( int i = 0; i < n; ++i )
		{
			//pf("i = %d dp1 = %d dp2 = %d\n",i, dp1[i], dp2[i]);
			ans = min( ans, dp1[i] + dp2[i+1] );
		}
		pf("Case #%d: %d\n",ca+1, ans);
	}

}
