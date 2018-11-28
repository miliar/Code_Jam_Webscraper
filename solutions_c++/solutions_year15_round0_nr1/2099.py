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

string word;

int main()
{
	ll t;
	cin>>t;
	for(ll counter=1; counter<=t; counter++)
	{

		ll n;
		cin>>n;
		cin>>word;

		ll cur = 0;
		ll ans = 0;
		for(ll i=0; i<=n; i++)
		{
			if(word[i]>'0' && cur<i)
			{
				ans += i-cur;
				cur += i-cur;
			}

			cur += word[i]-'0';

			//cout<<i<<" "<<ans<<" "<<cur<<endl;

		}

		cout<<"Case #"<<counter<<": ";
		cout<<ans<<endl;
	}
	return 0;
}