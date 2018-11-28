#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
__int64 n,p;

void init(){
	scanf("%I64d%I64d",&n,&p);
	n=1LL<<n;
	return;
}

__int64 checkbest(__int64 n,__int64 k){
	if ((k+1)==n){
		return n-1;
	}
	return checkbest(n/2,k-(k/2));
}

__int64 checkworst(__int64 n,__int64 k){
	if ((k+1)==n){
		return 0;
	}
	return checkworst(n/2,k-(k/2))+n/2;
}

__int64 good(){
	__int64 left=-1;
	__int64 right=n;
	while (right>left+1){
		__int64 mid=(left+right)/2;
		if (checkworst(n,n-mid-1)<p){
			left=mid;
		} else {
			right=mid;
		}
	}
	return left;
}

__int64 possible(){
	__int64 left=-1;
	__int64 right=n;
	while (right>left+1){
		__int64 mid=(left+right)/2;
		if (checkbest(n,mid)<p){
			left=mid;
		} else {
			right=mid;
		}
	}
	return left;
}


int main(){
	__int64 tcase;
	scanf("%I64d",&tcase);
	for (__int64 i=1;i<=tcase;i++){
		init();
		printf("Case #%I64d: %I64d %I64d\n",i,good(),possible());
	}
	return 0;
}
