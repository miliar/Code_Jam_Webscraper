#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>

using namespace std;


int ct;
int seen[10];

int check(int n){

	while(n){
		if(seen[n%10]){
			n /= 10;
			continue;
		}
		seen[n%10] =1;
		++ct;
		n /= 10;
		if(ct >= 10) return 1;
	}
	return 0;
}


int main(){

	int t,n,i;

	scanf("%d",&t);

	for(int x = 1; x <= t ; ++x){
		scanf("%d",&n);
		ct = 0;
		memset(seen,0,sizeof(seen));
		i = 1;

		if(!n){
			printf("Case #%d: Insomnia\n",x);
			continue;
		}

		while(1){
			if(check(n*i)){
				printf("Case #%d: %d\n",x,n*i);
				break;
			}
			++i;
		}
	}

	return 0;
}
