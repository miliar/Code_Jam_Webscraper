#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;
const int N = 1005;
int n,a[N];
void solve(){
	scanf("%d",&n);
	int maxK=0;
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
		maxK=max(maxK,a[i]);
	}
	int ans=1000;
	for(int k=1;k<=maxK;k++){
		int now=k;
		for(int i=0;i<n;i++){
			now+=(a[i]-1)/k;
		}
		ans=min(ans,now);
	}
	printf("%d\n",ans);
}
int main(){
	int T;
	scanf("%d",&T);
	for(int cas=0;cas<T;cas++){
		printf("Case #%d: ",cas+1);
		solve();
	}
	return 0;
}
