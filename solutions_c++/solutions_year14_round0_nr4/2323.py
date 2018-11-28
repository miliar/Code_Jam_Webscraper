#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define S(x) scanf("%lld", &x);
#define Sf(x) scanf("%lf", &x);
#define div /
int main()
{
	freopen("ttin", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;
	S(t);
	ll temp = 1;
	while(t--) {
		ll i,j;
		ll n;
		S(n);
		double nao[n + 5];
		double ken[n + 5];
		for(i= 0;i < n;i++) {
			Sf(nao[i]);
		}
		for(i= 0;i < n;i++) {
			Sf(ken[i]);
		}
		sort(nao, nao + n);
		sort(ken , ken + n);
		j = n- 1;
		ll r = 0;
		ll co1 = 0;
		for(i = n - 1;i >= 0&& j >= r;i--) {
			if(nao[j] < ken[i]) {
				r++;
			}
			else {
				j--;
				co1++;
			}
		}
		r = 0;
		ll co2 = 0;
		for(i = n- 1;i>= 0;i--) {
			ll in = -1;
			for(j = n - 1;j >= r;j--) {
				if(ken[j] > -1 && ken[j] > nao[i]) {
					in = j;	
				}
			}
			if(in == -1) {
				co2++;
				r++;
			}
			else {
				ken[in] = -1; 
			}
		}
		printf("Case #%lld: %lld %lld\n", temp++, co1, co2 );
	}
}


