//A_Mushroom Monster.cpp -- Google Code Jam Round A
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
typedef long long ll;
using namespace std;
const int maxn = 1000 + 10;
int n;
ll m[maxn];
int main()
{
	int T, ans = 0;
	scanf("%d", &T);
	while( T-- )
	{
		ll kry = 0, stal = 0;
		scanf("%d", &n);
		for( int i=0; i<n; i++ )
			scanf("%lld", &m[i]);
		ll Max = 0;
		for( int i=0; i<n-1; i++ )
		{
			if( m[i]>m[i+1] )
			{
				kry += m[i] - m[i+1];
				Max = max(Max, m[i]-m[i+1]);
			}
		}
		for( int i=0; i<n-1; i++ )
			stal += min(m[i], Max);
		printf("Case #%d: %lld %lld\n", ++ans, kry, stal);
	}
	return 0;
}
