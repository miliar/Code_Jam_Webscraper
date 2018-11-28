#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll modular_pow(ll base, ll exponent)
{
    ll result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base);
        exponent = exponent >> 1;
        base = (base * base);
    }
    return result;
}

int main(){
	
	freopen("input.txt", "r" , stdin);
	freopen ("output.txt","w",stdout);
	
	int t,r;
	scanf("%d",&t);
	
	ll k,c,s,i;
	
	for(r=1;r<=t;++r){
		scanf("%lld %lld %lld",&k,&c,&s);
		printf("Case #%d: ",r);
		if(k==1){
			printf("1\n");
			continue;	
		} 
		ll delta=modular_pow(k,c-1);
		delta=delta-1;
		delta=delta*k;
		delta=delta/(k-1);
		for(i=1;i<=s;++i){
			ll temp=(i-1)*delta;
			temp+=i;
			printf("%lld ",temp);
		}
		printf("\n");
	}
	
	fclose(stdout);
	return 0;
}
