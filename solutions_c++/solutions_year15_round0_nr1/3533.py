#include<stdio.h>
#include<string.h>
#define ll long long

using namespace std;

char ar[1004];

int main(){
	ll tt;
	scanf("%lld",&tt);
	for(ll i=1;i<=tt;i++){
		printf("Case #%lld: ",i);
		ll n;
		scanf("%lld",&n);
		scanf("%s",ar);
		if(n==0)
			printf("0\n");
		else{
			ll pws=0;
			ll ans=0;
			for(ll lv=0;lv<=n;lv++){
				if(lv<=pws){
					pws=pws+ar[lv]-48;
				}
				else{
					ans=ans+lv-pws;
					pws=lv;
					pws=pws+(ar[lv]-48);
				}
			}
			printf("%lld\n",ans);
		}
	}
	return 0;
}
