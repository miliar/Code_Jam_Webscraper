/*
 * Counting_sheep.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: 2016-04-09
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

ll f(ll n)
{
	if(n == 0) return n;
	bool a[10] = {};
	ll m, r, count = 0, ans;
	
	for(ll i=1; count < 10; i++){
		ans = m = n*i;
		while(m>0){
			r = m%10;
			if(a[r] == false){
				a[r] = true;
				count++;
			}
			m/=10;
		}
	}
	return ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output", "w", stdout);
	
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		ll n;
		scanf("%lld", &n);
		
		ll res = f(n);
		printf("Case #%d: ", ++cs);
		if(res == 0) puts("INSOMNIA");
		else printf("%lld\n", res);
	}

	return 0;
}

