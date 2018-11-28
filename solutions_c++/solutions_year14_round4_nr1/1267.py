#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <iomanip>
#include <string>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>

#define X first
#define Y second
#define ll long long
#define mp make_pair
#define pb push_back

using namespace std;
int a[710], n, mx;
int solve()
{
	int ans=0;
	scanf("%d%d", &n, &mx);
	memset(a, 0, sizeof(a));
	for (int i=1; i<=n; i++)
	{
		int x;
		scanf("%d", &x);
		a[x]++;
	}

	for (int i=700; i>0; i--)
	{
		if ( a[i]==0 ) continue;
		//cout<<i<<endl;
		if ( 2*i<=mx )
		{
			ans+=a[i]/2;
			a[i]%=2;
		}
		for (int j=min(i-1, mx-i); j>0 && a[i]>0; j--)
		{
			if (a[j]>0)
			{
				int t=min(a[j], a[i]);
				ans+=t;
				a[j]-=t; a[i]-=t;
			}
		}
		if ( a[i]>0 ) ans+=a[i], a[i]=0;
	}
	//cout<<ans<<endl;
	return ans;
}
int main()
{	
	freopen("abig.in", "r", stdin);
	freopen("abig.out", "w", stdout);
	int test;
	cin>>test;
	for (int i=1; i<=test; i++)
		printf("Case #%d: %d\n", i, solve());
	return 0;    
}

