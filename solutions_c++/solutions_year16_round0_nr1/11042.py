#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

typedef long long ll;

ll n;

int t;

bool foi[10];

int main(){
	
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &t);
	
	for(int c=1; c<=t; c++){
		
		memset(foi, false, sizeof foi);
	
		scanf("%lld", &n);
		
		if(n==0){
			
			printf("Case #%d: INSOMNIA\n", c);
			
			continue;
		}
		
		for(ll i=1;; i++){
			
			ll k=n*i;
			
			while(k>0){
				
				foi[k%10]=true;
				k/=10;
			}
			
			bool shit=false;
			
			for(int j=0; j<10; j++) if(!foi[j]) shit=true;
			
			if(!shit){
				
				printf("Case #%d: %lld\n", c, n*i);
				
				break;
			}
		}
	}
	
	return 0;
}