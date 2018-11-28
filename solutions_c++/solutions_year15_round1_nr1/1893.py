#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int n;
int M[1005];

int F1(){
	int ret=0;
	for (int i=1;i<n;++i) ret+=max(0,M[i-1]-M[i]);		
	return ret;
}

int F2(){
	int ret=0;
	int maxRate=0;
	for (int i=1;i<n;++i)maxRate=max(maxRate,M[i-1]-M[i]);
	for (int i=0;i<n-1;++i){
		ret+=min(maxRate,M[i]);
	}
	return ret;
}

int main() {
	int T;scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d",&n);	
		for (int i=0;i<n;++i)scanf("%d",M+i);
		
		printf("Case #%d: %d %d\n", t, F1(), F2());
	}
	return 0;
}
