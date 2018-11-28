#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>
#include <math.h>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long
#define ull unsigned long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )

using namespace std;

int a[10000];


int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		int n;
		cin>>n;
		int sum = 0;
		int max_ans = 0;
		fr(i,0,n)
		{
			sf("%d",&a[i]);
			sum += a[i];
			max_ans = max( a[i], max_ans );
		}
		int ans = max_ans;
		for( int i = 1; i <= max_ans; ++i )
		{
			int ct = 0;
			for( int  j = 0; j < n ;++j )
			{
				if( a[j] > i )
				{
					ct += ( a[j] + i - 1 )/i - 1;
				}
			}

			ans = min( ct + i, ans );
			//pf("ct = %d ans = %d\n",ct,ans);
		}
		pf("Case #%d: %d\n", c+1, ans);
	}

}

