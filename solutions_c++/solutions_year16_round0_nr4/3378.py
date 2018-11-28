#include <bits/stdc++.h>
using namespace std;
#define ll long long 

#define II pair <ll,ll>
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mod 1000000007

#define chk1(a) cout<<#a<<" = "<<a<<'\n'
#define chk2(a,b) cout<<#a<<" = "<<a<<' '<<#b<<" = "<<b<<'\n'
#define chk3(a,b,c) cout<<#a<<" = "<<a<<' '<<#b<<" = "<<b<<' '<<#c<<" = "<<c<<'\n'
#define chk4(a,b,c,d) cout<<#a<<" = "<<a<<' '<<#b<<" = "<<b<<' '<<#c<<" = "<<c<<' '<<#d<<" = "<<d<<'\n'
ll power(ll base, ll exponent)
  {
    ll result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)      
		 result = (result * base) ;
        exponent = exponent >> 1;
        base = (base * base) ;
    }
    return result;
}
int main()
{
	ll t,tc=1;ll i,c,k,p,num,s;
	scanf("%lld",&t);

	while(t--) {
		printf("Case #%lld: ",tc++);
		scanf("%lld %lld %lld",&k,&c,&s);
		num=1;
		p=power(k,c-1);
		for(i=1;i<=k;i++) {
			printf("%lld ",num);
			num+=p;
		}
		printf("\n");
	}	
	return 0;
}
