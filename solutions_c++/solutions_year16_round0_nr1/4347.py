#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
#define ull unsigned long long 
int n;
int a[10];
int solve(ull c){
	while(c){
		a[c%10]=1;
		c/=10;
	}
	int res=0;
	for(int i=0;i<10;i++){
		res+=a[i];
	}
	return res;
}
int main(){
	int t;
	scanf("%d",&t);
	int time=0;
	while(t--){
		time++;
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		if(!n){
			printf("Case #%d: INSOMNIA\n",time);
			continue;
		}
		if(solve(n)==10){
			printf("Case #%d: %d\n",time,n);
			continue;
		} 
		ull tmp;
		for(int i=2;;i++){
			tmp=i*n;
			if(solve(tmp)==10){
				printf("Case #%d: %lld\n",time,tmp);
				break;
			}
		}
	}
	return 0;
}
