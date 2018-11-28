#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	freopen("inpu", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll tc;
	cin>>tc;
	ll temp = 1;
	while(tc--) {
		ll i,j,n;
		cin>>n;
		double nao[n + 5];
		double ken[n + 5];
		for(i= 0;i < n;i++) {
			cin>>nao[i];
		}
		for(i= 0;i < n;i++) {
			cin>>ken[i];
		}
		sort(nao, nao + n);
		sort(ken , ken + n);
		j = n- 1;
		ll a = 0;
		ll co1 = 0;
		for(i = n - 1;i >= 0&& j >= a;i--) {
			if(nao[j] < ken[i]) {
				a++;
			}
			else {
				j--;
				co1++;
			}
		}
		a = 0;
		ll co2 = 0;
		for(i = n- 1;i>= 0;i--) {
			ll in = -1;
			for(j = n - 1;j >= a;j--) {
				if(ken[j] > -1 && ken[j] > nao[i]) {
					in = j;	
				}
			}
			if(in == -1) {
				co2++;
				a++;
			}
			else {
				ken[in] = -1; 
			}
		}
		printf("Case #%lld: %lld %lld\n", temp++, co1, co2 );
	}
	return 0;
}


