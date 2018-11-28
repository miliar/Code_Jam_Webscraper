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
const __int64 maxn=10000001;
__int64 cnt[maxn];
__int64 a,b;

bool check(__int64 k){
	__int64 cur=k;
	char digi[16];
	__int64 len=0;
	while (true){
		if (cur==0){
			break;
		}
		digi[len]=cur%10;
		cur/=10;
		len++;
	}
	for (__int64 i=0;i<len;i++){
		if (digi[i]!=digi[len-i-1]){
			return false;
		}
	}
	return true;
}

void preprocess(){
	memset(cnt,0,sizeof(cnt));
	for (__int64 i=1;i<maxn;i++){
		cnt[i]=cnt[i-1];
		if (check(i)&&check(i*i)){
			cnt[i]++;
		}
	}
	return;
}

void init(){
	scanf("%I64d%I64d",&a,&b);
	return;
}

int main(){
	preprocess();
	__int64 tcase;
	scanf("%I64d",&tcase);
	for (__int64 i=1;i<=tcase;i++){
		init();
        printf("Case #%I64d: %I64d\n",i,cnt[((int)sqrt(((double)b)))]-cnt[((int)sqrt(((double)a)-1.0))]);
	}
	return 0;
}
