#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>
using namespace std;
int dig[10];
int cnt = 0;
inline void add(long long x){
	while(x){
		if(!dig[x%10]){
			cnt ++;
			dig[x%10] = 1;
		}
		x /= 10;
	}
}
int main(){
	int tcase;
	cin >> tcase;
	for(int casei=1;casei<=tcase;casei++){
		long long n;
		long long now = 0;
		cin >> n;
		if(!n){
			printf("Case #%d: INSOMNIA\n",casei);
			continue;
		}
		memset(dig,0,sizeof(dig));
		cnt = 0;
		while(cnt < 10){
			now += n;
			add(now);
		}
		printf("Case #%d: %lld\n",casei,now);
	}
	return 0;
}
