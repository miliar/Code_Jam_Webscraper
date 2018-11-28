#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <memory.h>
#include <queue>
#include <map>

using namespace std;


typedef long long ll;
const ll N = 600000;


ll cur = 0,ca = 0;
map<int,int> freq;
vector<int> digits;

int t;

int main(){
	scanf("%d",&t);
	while(t--){
		int cnt = 0;
		freq.clear();
		scanf("%lld",&cur);
		printf("Case #%d: ",++ca);
		for(ll step = 1 ; step <= N;step++){
			digits.clear();
			ll x = step * cur;
			while(x > 0){
				if(freq[(x % 10)] == 0){
				 	freq[(x % 10)]++;
				 	cnt++;
				}
				x /=10;
			}
			if(cnt == 10){
				printf("%lld\n",step * cur);
				break;
			}
		}
		if(cnt != 10){
			puts("INSOMNIA");
		}
	}
	return 0;
}
