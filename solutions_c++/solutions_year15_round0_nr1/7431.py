#include <bits/stdc++.h>

using namespace std;
#define ll long long int
int main()
{
	ll t;
	ll shy;
	ll count,ans;
	char audience[1010];

	scanf("%lld",&t);
	
	for(ll j = 1;j <= t;j++)
	{
		scanf("%lld",&shy);
		scanf("%s",audience);
		count = 0;
		ans = 0;

		ll l = strlen(audience);

		for(ll i = 0;i < l;i++){
			if(count < i && audience[i] != '0'){

				ans = ans + (i - count);
				count = count + (i - count) + (audience[i]-'0');
			}
			else if(count >= i)
				count = count + (audience[i]-'0');
		}

		printf("Case #%lld: %lld\n",j,ans);
	}
	return 0;
}
