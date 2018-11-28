#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define S(x) scanf("%lld", &x);
#define Sf(x) scanf("%lf", &x);
#define div /
double a[100005];
double b[100005];
double su[100005];
int main()
{
	freopen("innn", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t;
	S(t);
	ll i;
	for(i = 1;i <= t;i++) {
		ll j,k;
		double c,f,x;
		Sf(c);
		Sf(f);
		Sf(x);
		double mi = INT_MAX;
		su[0] = 0.0;
		b[0] = 2.0;
		mi = x div b[0];
 		for(j = 1;j <= 100000;j++) {
			a[j] = c div b[j - 1];
			b[j] = b[j- 1] + f;
			su[j] = su[j - 1]+a[j];
			if(mi > su[j] + (x div b[j])) {
				mi = su[j] + (x div b[j]);
			}
			else {
				break;
			}
		}
		printf("Case #%lld: %0.7lf\n", i,mi);
	}
}


