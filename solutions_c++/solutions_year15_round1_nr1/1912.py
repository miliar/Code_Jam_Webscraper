/* 
 * CodeJam 2015
 * Google
 * Date : 18/04/2015
 */
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;

typedef long long ll;

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	ll t,n;
	scanf("%lld",&t);
	for(ll k=1;k<=t;k++){
		
		scanf("%lld",&n);
		vector<ll> m(n);
		for(ll i=0;i<n;i++){
			scanf("%lld",&m[i]);
		}
		//finding max difference
		ll constantRate = 0;
		for(ll i=1;i<n;i++){
			if( (m[i-1] - m[i]) > constantRate ) {
				constantRate = m[i-1] - m[i];
			}
		}
		//first method of eating
		ll firstMin = 0;
		for(ll i=1;i<n;i++){
			if(m[i-1] > m[i] ){
				firstMin += m[i-1] - m[i];
			}
		}
		//second method of eating
		ll secondMethod = 0;
		for(ll i=0;i<n-1;i++){
			secondMethod += min(m[i],constantRate);
		}

		//printing answer 
		printf("Case #%lld: %lld %lld\n",k,firstMin,secondMethod );

	}

	return 0;
}
/********************************* END OF PROGRAM **************************/
