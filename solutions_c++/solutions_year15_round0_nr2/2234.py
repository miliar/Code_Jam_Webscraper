#include <cstdio>
#include <iostream>
using namespace std;
int T,n,a[10005];
int cal(int x){
   int ret=0;
   for (int i=0;i<n;i++){
	   ret+=(a[i]-1)/x;
   }
   return ret+x;
}


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-small.out","w",stdout);
	scanf("%d",&T);
	int ca=1;
	while(T--){
		int ans=1005;
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%d",&a[i]);
		for (int i=1;i<=1000;i++){
			ans=min(ans,cal(i));
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
}
