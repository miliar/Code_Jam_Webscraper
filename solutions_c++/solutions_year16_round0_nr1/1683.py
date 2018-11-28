#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
int n,got,have[15];
void work(long long x){
	while(x){
		int tmp=x%10;
		if(!have[tmp]){
			have[tmp]=true;
			got++;
		}
		x/=10;
	}
}
int main(){
	int T,ca=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		if(n==0) {
			printf("Case #%d: INSOMNIA\n",ca++);
			continue;
		}
		got=0;
		memset(have,0,sizeof(have));
		long long now=n;
		while(got<10){
			work(now);
			if(got>=10) break;
			now+=n;
		}
		printf("Case #%d: %lld\n",ca++,now);
	}
	return 0;
}
