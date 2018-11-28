#include <iostream>
#include <cstdio>
#define ll long long
using namespace std;

bool f[10];
bool k;
int t;
ll n;



int main() {
	// your code goes here
	
	scanf("%d",&t);
	
	for(int ii=1;ii<=t;ii++){
		scanf("%lld",&n);
		if(n==0) {
			printf("Case #%d: INSOMNIA\n",ii);
			continue;
		}
		for(int i=0;i<10;i++) f[i] = false;
		k = false;
		ll count = 1;
		ll copy = n;
		while(!k){
			n = copy * count;
			count++;
			bool p = false;
			ll q = n;
			
			while(q>0){
			
				ll temp = q%10;
				q/=10;
				f[temp] = true;
			}
			
			for(ll i=0;i<10;i++){
				if(!f[i]){
					p = true;
					break;
				}
			}
			
			if(!p)
				k = true;
			
		}
		printf("Case #%d: %lld\n",ii,n);
	}
	
	return 0;
}
