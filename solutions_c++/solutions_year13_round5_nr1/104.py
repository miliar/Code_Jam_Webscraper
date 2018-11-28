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
const __int64 maxn=37;
__int64 b,n;
__int64 x[maxn];

void init(){
	scanf("%I64d%I64d",&b,&n);
	memset(x,0,sizeof(x));
	for (__int64 i=0;i<n;i++){
		scanf("%I64d",&x[i]);
	}
	sort(x,x+37);
	return;
}

double calc(){
	double ans=0;
	for (__int64 i=1;i<37;i++){
		__int64 left=-1;
		__int64 right=2251799813685248LL;
		__int64 cost=0;
		__int64 delta=0;
		while (true){
			if (left>=right-1){
				break;
			}
			__int64 mid=(left+right)/(2LL);
			__int64 tcost=0;
			__int64 tdelta=0;
			for (__int64 j=0;j<i;j++){
				if (x[j]>mid){
					continue;
				}
				tcost+=mid-x[j];
			}
			for (__int64 j=i;j<37;j++){
				if (x[j]>mid){
					continue;
				}
				tdelta+=mid-x[j]+1LL;
			}
			if (b>=tcost+tdelta){
				left=mid;
				cost=tcost;
				delta=tdelta;
			} else {
				right=mid;
			}
		}
		ans=max(ans,((double)cost)*(36.0-((double)i))/((double)i)-delta);
	}
	return ans;
}

int main(){
	__int64 tcase;
	scanf("%I64d",&tcase);
	for (__int64 i=1;i<=tcase;i++){
		init();
		printf("Case #%I64d: %.8lf\n",i,calc());
	}
	return 0;
}
