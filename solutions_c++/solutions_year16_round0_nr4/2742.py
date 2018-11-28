#include <bits/stdc++.h>

#define ll long long
using namespace std;

ll k,c,s;

int main(){
	
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-output.txt","w",stdout);
	
	int teskes;
	scanf("%d",&teskes);
	
	for(int tc=1;tc<=teskes;tc++){
		scanf("%lld%lld%lld",&k,&c,&s);
		
		ll temp=k;
		for(ll x=1;x<c;x++)temp*=k;
		
		ll sp = temp/k;
		ll now = 1;
		
		printf("Case #%d:",tc);
		while(now<=temp){
			printf(" %lld",now);
			now+=sp;
		}
		printf("\n");
	}
	
	return 0;
}
