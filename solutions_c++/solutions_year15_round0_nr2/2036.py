#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <math.h>

#define max_nodes_size 100005
#define max_log_size 17
#define ll int
#define mod 1000000007

#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define INF 0x3f3f3f3f
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
	
using namespace std;

ll diners[1005];

int main()
{
	ll t;
	cin>>t;
	for(ll counter=1; counter<=t; counter++)
	{
		ll n;
		cin>>n;

		ll ans = 0;
		for(ll i=0; i<n; i++)
		{
			cin>>diners[i];
			ans = max(ans, diners[i]);
		}

		ll temp = ans;
		for(ll i=1; i<=temp; i++)
		{
			ll req_time = 0;
			for(ll j=0; j<n; j++)
			{
				req_time += diners[j]/i;
				if(diners[j]%i==0)
					req_time--;
			}

			req_time += i;

			//cout<<i<<" "<<req_time<<endl;

			ans = min(ans, req_time);
		}
		
		cout<<"Case #"<<counter<<": ";
		cout<<ans<<endl;
	}
	return 0;
}