#include <cstring>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int T;
int a[1005];
int n;
int main(){
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		int ans=0;
		for (int i=0;i<n;i++){
			int tmp=0;
			for (int j=0;j<i;j++){
				if(a[j]>a[i]) tmp++;
			}
			int tmp1=0;
			for (int j=i+1;j<n;j++){
				if(a[j]>a[i])tmp1++;
			}
			ans+=min(tmp,tmp1);
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}
